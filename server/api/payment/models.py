from __future__ import annotations
from typing import List

import uuid
from django.db import models

from api.products import models as products_models
from .settings import get_config_value


class PaymentModel(models.Model):
    RESPONSE_FIELDS = {
        'Success': 'success',
        'Status': 'status',
        'PaymentId': 'payment_id',
        'ErrorCode': 'error_code',
        'PaymentURL': 'payment_url',
        'Message': 'message',
        'Details': 'details',
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    amount = models.IntegerField(verbose_name='Сумма в копейках', editable=False)
    order_id = models.CharField(verbose_name='Номер заказа', max_length=100, editable=False)
    description = models.TextField(verbose_name='Описание', max_length=250, blank=True, default='', editable=False)

    success = models.BooleanField(verbose_name='Успешно проведен', default=False, editable=False)
    status = models.CharField(verbose_name='Статус транзакции', max_length=20, default='', editable=False)
    payment_id = models.CharField(
        verbose_name='Уникальный идентификатор транзакции в системе банка', max_length=20, default='', editable=False)
    error_code = models.CharField(verbose_name='Код ошибки', max_length=20, default='', editable=False)
    payment_url = models.CharField(
        verbose_name='Ссылка на страницу оплаты.',
        help_text='Ссылка на страницу оплаты. По умолчанию ссылка доступна в течении 24 часов.',
        max_length=100, blank=True, default='', editable=False)
    message = models.TextField(verbose_name='Краткое описание ошибки', blank=True, default='', editable=False)
    details = models.TextField(verbose_name='Подробное описание ошибки', blank=True, default='', editable=False)

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return f'Транзакция #{self.pk}:{self.order_id}:{self.payment_id}'

    def can_redirect(self) -> bool:
        return self.status == 'NEW' and self.payment_url

    def is_paid(self) -> bool:
        return self.status == 'CONFIRMED' or self.status == 'AUTHORIZED'

    def with_receipt(self, email: str = '', phone: str = '') -> PaymentModel:
        if not self.id:
            self.save()

        if hasattr(self, 'receipt'):
            return self
        
        email = email or get_config_value('RECEIPT_EMAIL')
        phone = phone or get_config_value('RECEIPT_PHONE')

        ReceiptModel.objects.create(payment=self, email=email, phone=phone)

        return self

    def with_items(self, items: List[dict]) -> PaymentModel:
        for item in items:
            ReceiptItemModel.objects.create(**item, receipt=self.receipt)
        return self

    @staticmethod
    def create(**kwargs):
        try:
            payment = PaymentModel.objects.get(
                order_id=kwargs.get('order_id'),
            )

            return payment
        except PaymentModel.DoesNotExist:
            return PaymentModel.objects.create(**kwargs)

    @staticmethod
    def get(**kwargs):
        try:
            payment = PaymentModel.objects.get(
                order_id=kwargs.get('order_id'),
            )

            return payment
        except PaymentModel.DoesNotExist:
            return PaymentModel.objects.get(**kwargs)

    def to_json(self) -> dict:
        data = {
            'Amount': self.amount,
            'OrderId': self.order_id,
            'Description': self.description,
        }

        if hasattr(self, 'receipt'):
            data['Receipt'] = self.receipt.to_json()

        return data


class ReceiptModel(models.Model):
    payment = models.OneToOneField(
        PaymentModel, models.CASCADE,
        related_name="receipt",
        verbose_name='Платеж'
    )
    email = models.CharField(
        verbose_name='Электронный адрес для отправки чека покупателю', max_length=64)
    phone = models.CharField(verbose_name='Телефон покупателя', max_length=64, blank=True, default='')

    class Meta:
        verbose_name = 'Данные чека'
        verbose_name_plural = 'Данные чеков'

    def __str__(self):
        return f'{self.pk} ({self.payment})'

    def to_json(self) -> dict:
        return {
            'Email': self.email,
            'Phone': self.phone,
            'Taxation': get_config_value('TAXATION'),
            'Items': [item.to_json() for item in self.receiptitem.all()]
        }


class ReceiptItemModel(models.Model):
    receipt = models.ForeignKey(
        ReceiptModel, models.CASCADE,
        related_name="receiptitem",
        verbose_name='Чек'
    )
    product = models.ForeignKey(
        products_models.ProductModel, models.PROTECT,
        verbose_name='Товар',
        null=True, blank=True
    )
    name = models.CharField(
        verbose_name='Название', max_length=255,
        null=True, blank=True
    )
    price = models.IntegerField(verbose_name='Цена в копейках')
    quantity = models.IntegerField(verbose_name='Количество')
    amount = models.IntegerField(verbose_name='Сумма в копейках')

    class Meta:
        verbose_name = 'Информация о товаре'
        verbose_name_plural = 'Информация о товарах'

    def __str__(self):
        return f'{self.pk} (Чек {self.receipt.pk})'

    def save(self, *args, **kwargs):
        if not self.amount:
            self.amount = self.price * self.quantity

        return super().save(*args, **kwargs)

    def to_json(self) -> dict:
        return {
            'Name': self.product.name if self.product else self.name,
            'Price': self.price,
            'Quantity': self.quantity,
            'Amount': self.amount,
            'Tax': get_config_value('ITEM_TAX'),
        }
