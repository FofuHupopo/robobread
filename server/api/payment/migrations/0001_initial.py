# Generated by Django 5.0.6 on 2024-05-21 16:25

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField(editable=False, verbose_name='Сумма в копейках')),
                ('order_id', models.CharField(editable=False, max_length=100, verbose_name='Номер заказа')),
                ('description', models.TextField(blank=True, default='', editable=False, max_length=250, verbose_name='Описание')),
                ('success', models.BooleanField(default=False, editable=False, verbose_name='Успешно проведен')),
                ('status', models.CharField(default='', editable=False, max_length=20, verbose_name='Статус транзакции')),
                ('payment_id', models.CharField(default='', editable=False, max_length=20, verbose_name='Уникальный идентификатор транзакции в системе банка')),
                ('error_code', models.CharField(default='', editable=False, max_length=20, verbose_name='Код ошибки')),
                ('payment_url', models.CharField(blank=True, default='', editable=False, help_text='Ссылка на страницу оплаты. По умолчанию ссылка доступна в течении 24 часов.', max_length=100, verbose_name='Ссылка на страницу оплаты.')),
                ('message', models.TextField(blank=True, default='', editable=False, verbose_name='Краткое описание ошибки')),
                ('details', models.TextField(blank=True, default='', editable=False, verbose_name='Подробное описание ошибки')),
                ('payment_fail', models.BooleanField(default=False, verbose_name='Ошибка платежа')),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64, verbose_name='Электронный адрес для отправки чека покупателю')),
                ('phone', models.CharField(blank=True, default='', max_length=64, verbose_name='Телефон покупателя')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payment.payment', verbose_name='Платеж')),
            ],
            options={
                'verbose_name': 'Данные чека',
                'verbose_name_plural': 'Данные чеков',
            },
        ),
        migrations.CreateModel(
            name='ReceiptItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена в копейках')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('amount', models.IntegerField(verbose_name='Сумма в копейках')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.productmodel', verbose_name='Товар')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.receipt', verbose_name='Чек')),
            ],
            options={
                'verbose_name': 'Информация о товаре',
                'verbose_name_plural': 'Информация о товарах',
            },
        ),
    ]
