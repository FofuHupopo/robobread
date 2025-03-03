import uuid

from django.utils import timezone
from django.db import models


class MachineModel(models.Model):
    name = models.CharField(
        "Название автомата",
        max_length=255,
    )
    address = models.CharField(
        "Адрес автомата",
        max_length=255,
    )
    sku = models.CharField(
        "SKU",
        max_length=255,
        unique=True,
    )

    token = models.UUIDField(
        "Токен",
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    class Meta:
        verbose_name = "Автомат"
        verbose_name_plural = "Автоматы"

    def __str__(self):
        return f"<MachineModel {self.name=}, {self.sku=}>"


class MachineOrderModel(models.Model):
    machine = models.ForeignKey(
        MachineModel,
        on_delete=models.CASCADE,
    )
    
    order_id = models.UUIDField(
        "ID заказа",
    )

    product_sku = models.CharField(
        verbose_name='Артикул товара',
        max_length=128,
    )

    amount = models.IntegerField(
        verbose_name='Стоимость в копейках',
        default=0,
    )

    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        default=timezone.now,
    )

    is_paid = models.BooleanField(
        verbose_name='Оплачено?',
        default=False,
    )

    @staticmethod
    def key():
        return "order_id"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        unique_together = ('machine', 'order_id')

    def __str__(self):
        return f"<MachineOrderModel machine_sku={self.machine.sku}, order_id={self.order_id}>"


class MachineCategoryModel(models.Model):
    machine = models.ForeignKey(
        MachineModel,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        "Название категории",
        max_length=255,
    )
    sku = models.CharField(
        "SKU",
        max_length=128,
    )

    @staticmethod
    def key():
        return "sku"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ('machine', 'sku')

    def __str__(self):
        return f"<MachineCategoryModel machine_sku={self.machine.sku}, sku={self.sku}>"


class MachineProductModel(models.Model):
    machine = models.ForeignKey(
        MachineModel,
        on_delete=models.CASCADE,
    )
    sku = models.CharField(
        "SKU",
        max_length=128,
    )
    
    name = models.CharField(
        "Название товара",
        max_length=255,
    )
    description = models.TextField(
        "Описание",
        null=True, blank=True,
    )
    composition = models.TextField(
        "Состав",
        null=True, blank=True,
    )
    
    category_sku = models.CharField(
        "SKU категории",
        max_length=128,
    )
    
    expiration_date = models.DurationField(
        "Срок годности",
        default=timezone.timedelta(0),
    )

    price = models.IntegerField(
        "Стоимость (в копейках)",
        default=0,
    )

    @staticmethod
    def key():
        return "sku"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        unique_together = ('machine', 'sku')

    def __str__(self):
        return f"<MachineProductModel machine_sku={self.machine.sku}, sku={self.sku}>"


class MachineCellModel(models.Model):
    machine = models.ForeignKey(
        MachineModel,
        on_delete=models.CASCADE,
    )
    
    number = models.IntegerField(
        "Номер ячейки",
    )
    count = models.IntegerField(
        "Количество",
    )
    max_count = models.IntegerField(
        "Максимальное количество",
    )

    product_sku = models.CharField(
        "SKU товара",
        max_length=128,
    )

    @staticmethod
    def key():
        return "number"

    class Meta:
        verbose_name = "Ячейка"
        verbose_name_plural = "Ячейки"
        unique_together = ('machine', 'number')

    def __str__(self):
        return f"<MachineCellModel machine_sku={self.machine.sku}, number={self.number}>"


class MachineProductInCellModel(models.Model):
    machine = models.ForeignKey(
        MachineModel,
        on_delete=models.CASCADE,
    )
    
    product_in_cell_id = models.IntegerField(
        "ID записи в автомате",
    )
    cell_number = models.IntegerField(
        "Номер ячейки",
    )
    upload_date = models.DateTimeField(
        "Дата загрузки",
    )
    expiration_date = models.DurationField(
        "Срок годности",
        blank=True, null=True,
    )

    @staticmethod
    def key():
        return "product_in_cell_id"

    class Meta:
        verbose_name = "Товар в ячейке"
        verbose_name_plural = "Товары в ячейках"
        unique_together = ('machine', 'product_in_cell_id')

    def __str__(self):
        return f"<MachineProductInCellModel machine_sku={self.machine.sku}, cell_number={self.cell_number}>"
