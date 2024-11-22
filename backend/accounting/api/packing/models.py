from django.db import models
from django.utils import timezone

from api.vending_machines.models import VendingMachineModel
from api.products.models import ProductModel


class PackingModel(models.Model):
    vending_machine = models.ForeignKey(
        VendingMachineModel, models.PROTECT,
        verbose_name="Торговый автомат"
    )
    
    packing_date = models.DateTimeField(
        "Дата затаривания", default=timezone.now
    )

    class Meta:
        db_table = "packing__packing"
        verbose_name = "История затаривания"
        verbose_name_plural = "Истории затаривания"

    def __str__(self) -> str:
        return f"{self.vending_machine.name} - {self.packing_date}"


class PackingAddedItemModel(models.Model):
    product = models.ForeignKey(
        ProductModel, models.PROTECT,
        verbose_name="Товар"
    )

    packing = models.ForeignKey(
        PackingModel, models.CASCADE,
        related_name="added_items"
    )

    count = models.IntegerField(
        "Количество", default=0
    )

    class Meta:
        db_table = "packing__packing_added_item"
        verbose_name = "Загруженный продукт"
        verbose_name_plural = "Загруженные продукты"
    
    def __str__(self) -> str:
        return f"{self.packing.vending_machine.name}: {self.product.name} - добавлено {self.count}"


class PackingRemovedItemModel(models.Model):
    product = models.ForeignKey(
        ProductModel, models.PROTECT,
        verbose_name="Товар"
    )

    packing = models.ForeignKey(
        PackingModel, models.CASCADE,
        related_name="removed_items"
    )

    count = models.IntegerField(
        "Количество", default=0
    )

    class Meta:
        db_table = "packing__packing_removed_item"
        verbose_name = "Выгруженный продукт"
        verbose_name_plural = "Выгруженные продукты"

    def __str__(self) -> str:
        return f"{self.packing.vending_machine.name}: {self.product.name} - удалено {self.count}"
