# Generated by Django 5.0.6 on 2024-05-21 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_payment_paymentmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptitemmodel',
            name='receipt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiptitem', to='payment.receiptmodel', verbose_name='Чек'),
        ),
        migrations.AlterField(
            model_name='receiptmodel',
            name='payment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receipt', to='payment.paymentmodel', verbose_name='Платеж'),
        ),
    ]