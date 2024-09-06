from typing import Type
import os

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone


def category_image_upload_path(instance: "CategoryModel", filename: str) -> str:
        return f"categories/{instance.sku}__{filename}"


class CategoryModel(models.Model):
    name = models.CharField(
        "Название", max_length=255
    )
    sku = models.CharField(
        "Артикул", unique=True, max_length=128
    )
    image = models.ImageField(
        "Изображение",
        default="default.jpeg",
        upload_to=category_image_upload_path
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = "products__categories"
        
    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"CategoryModel<name={self.name}>"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_image = CategoryModel.objects.get(pk=self.pk).image

            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

        super(CategoryModel, self).save(*args, **kwargs)


def product_image_upload_path(instance: "ProductModel", filename: str) -> str:
        return f"products/{instance.sku}__{filename}"


class ProductModel(models.Model):
    name = models.CharField(
        "Название", max_length=255
    )
    description = models.TextField(
        "Описание", default="",
        null=True, blank=True
    )
    composition = models.TextField(
        "Состав", default="",
        null=True, blank=True
    )

    sku = models.CharField(
        "Артикул", max_length=128, unique=True
    )
    
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE
    )

    expiration_date = models.DurationField(
        "Срок годности", default=timezone.timedelta(0)
    )

    price = models.IntegerField(
        "Стоимость (в копейках)", default=10000
    )

    image = models.ImageField(
        "Изображение",
        default="default.jpeg",
        upload_to=product_image_upload_path
    )

    @property
    def is_can_sell(self) -> bool:
        for cell in self.cells.all():
            cell: CellModel

            if cell.is_can_sell:
                return True

        return False

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        db_table = "products__products"
    
    def get_first_available_cell(self) -> "CellModel":
        for cell in self.cells.all():
            cell: CellModel

            if cell.is_can_sell:
                return cell
            
        return None
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return f"ProductModel<name={self.name}, category={self.category.name}>"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            old_image = ProductModel.objects.get(pk=self.pk).image

            if old_image and old_image != self.image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)

        super(ProductModel, self).save(*args, **kwargs)


class CellError(Exception):
    """
    Machine cell errors
    """
    def __call__(self, message):
        return f"{self.__class__.__name__}, {message}"


class CellModel(models.Model):
    number = models.IntegerField(
        "Номер ячейки", unique=True,
        blank=True, null=True
    )

    count = models.IntegerField(
        "Количество", default=0,
    )

    max_count = models.IntegerField(
        "Максимальное количество", default=10
    )

    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name="cells"
    )

    class Meta:
        verbose_name = "Ячейка"
        verbose_name_plural = "Ячейки"
        db_table = "products__cells"

    @property
    def is_can_sell(self) -> bool:
        if self.count <= 0 or self.products.count() <= 0:
            return False

        product_in_cell: ProductInCellModel = self.products.first()

        expiration_date = product_in_cell.upload_date + product_in_cell.expiration_date

        if expiration_date < timezone.now():
            return False
        
        return True

    @property
    def is_can_add_product(self) -> bool:
        return self.count < self.max_count

    def add_product(self, upload_date=None, expiration_date=None) -> "ProductInCellModel":
        product_detail = ProductInCellModel.objects.create(
            cell=self,
        )

        if upload_date:
            product_detail.upload_date = upload_date
        
        if expiration_date:
            product_detail.expiration_date = expiration_date

        product_detail.save()

        return product_detail
    
    def remove_product(self):
        self.products.first().delete()

    def __str__(self) -> str:
        return f"Номер: {self.number}, Товар: {self.product.name}"

    def __repr__(self) -> str:
        return f"<CellModel number={self.number}, product={self.product.name}>"


class ProductInCellModel(models.Model):
    cell = models.ForeignKey(
        CellModel, models.CASCADE,
        verbose_name="Ячейка",
        related_name="products"
    )

    upload_date = models.DateTimeField(
        "Дата загрузки", default=timezone.now
    )

    expiration_date = models.DurationField(
        "Срок годности",
        blank=True, null=True
    )

    class Meta:
        db_table = "products__product_details"
        verbose_name = "Товар в ячейке"
        verbose_name_plural = "Товары в ячейках"

    def save(self, *args, **kwargs) -> None:
        if not self.expiration_date and self.cell.product:
            self.expiration_date = self.cell.product.expiration_date

        if not self.pk and not self.cell.is_can_add_product:
            raise CellError("There is not enough space in the cell")

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.cell.product.name} в ячейке {self.cell.number} (срок годности: {self.upload_date + self.expiration_date})"


@receiver(post_save, sender=ProductInCellModel)
def create_product_in_cell(
        sender: Type[ProductInCellModel], instance: ProductInCellModel, created, **kwargs
    ):
    if not created:
        return

    instance.cell.count += 1
    instance.cell.save()


@receiver(pre_delete, sender=ProductInCellModel)
def delete_product_in_cell(
        sender: Type[ProductInCellModel], instance: ProductInCellModel, **kwargs
    ):
    instance.cell.count -= 1
    instance.cell.save()
