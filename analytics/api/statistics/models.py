from django.db import models

from api.core.models import VendingMachineModel


class SalesModel(models.Model):
    vending_machine = models.ForeignKey(
        VendingMachineModel, on_delete=models.CASCADE,
        related_name='sales_syncs',
    )
    sync_date = models.DateTimeField(auto_now_add=True)
    
    product_id = models.IntegerField()
    product_name = models.CharField(
        max_length=200, default=""
    )

    category_id = models.IntegerField()
    category_name = models.CharField(max_length=200)

    order_id = models.CharField(max_length=256, unique=True)
    
    amount = models.IntegerField()
    created_at = models.DateTimeField()

    is_paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'sales'
        verbose_name = "Продажа"
        verbose_name_plural = "Продажи"

    def __str__(self):
        return f"SalesModel<>"
    

class ProductStockModel(models.Model):
    vending_machine = models.ForeignKey(
        VendingMachineModel, on_delete=models.CASCADE,
        related_name='product_stocks',
    )
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    max_quantity = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'products_stock'
        verbose_name = "Товарный остаток"
        verbose_name_plural = "Товарные остатки"

    def __str__(self):
        return f"{self.product_name}: {self.quantity} in {self.vending_machine.name}"
