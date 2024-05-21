import uuid
from django.db import models
from django.utils import timezone

from api.products import models as products_models


class OrderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    product = models.ForeignKey(
        products_models.ProductModel, models.PROTECT,
        verbose_name="Товар"
    )
    
    amount = models.IntegerField(
        verbose_name='Стоимость в копейках',
        default=0
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now,
    )

    paid_at = models.DateTimeField(
        verbose_name='Дата создания',
        null=True, blank=True
    )

    is_paid = models.BooleanField(
        verbose_name='Оплачено?',
        default=False
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'orders_orders'

    def __str__(self):
        return f'Заказ #{self.id}'
    
    def paid(self):
        self.is_paid = True
        self.paid_at = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        self.amount = self.product.price

        return super().save(*args, **kwargs)
