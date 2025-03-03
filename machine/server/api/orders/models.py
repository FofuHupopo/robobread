import uuid
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete

from api.products import models as products_models
from api.synchronizer import SynchronizerEndpoints, SyncableModel


class OrderModel(SyncableModel):
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
    
    @staticmethod
    def sync_endpoint():
        return SynchronizerEndpoints.ORDER
    
    @staticmethod
    def key() -> str:
        return "order_id"
    
    def to_dict(self):
        return {
            'order_id': str(self.id),
            'product_sku': self.product.sku,
            'amount': self.amount,
            'created_at': str(self.created_at),
            'is_paid': self.is_paid,
        }


@receiver(pre_save, sender=OrderModel)
def syncable_saved(sender, instance: SyncableModel, **kwargs):
    if not instance.is_sync:
        instance.sync()


@receiver(pre_delete, sender=OrderModel)
def syncable_removed(sender, instance: SyncableModel, **kwargs):
    instance.remove()
