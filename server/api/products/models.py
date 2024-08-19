from django.db import models
import json


def category_image_upload_path(instance: models.Model, filename: str) -> str:
        return f"categories/{instance.pk}/{filename}"


class CategoryModel(models.Model):
    name = models.CharField(
        "Название", max_length=255
    )
    image = models.ImageField(
        "Изображение",
        default="categories/default.png",
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


def product_image_upload_path(instance: models.Model, filename: str) -> str:
        return f"products/{instance.pk}/{filename}"


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
    
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE
    )

    price = models.IntegerField(
        "Стоимость (в копейках)", default=10000
    )

    image = models.ImageField(
        "Изображение",
        default="products/default.png",
        upload_to=product_image_upload_path
    )

    @property
    def is_empty(self) -> bool:
        for cell in self.cells.all():
            if cell.count > 0:
                return False

        return True

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        db_table = "products__products"
    
    def get_first_not_empty_cell(self) -> "CellModel":
        for cell in self.cells.all():
            if cell.count > 0:
                return cell
            
        return None
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return f"ProductModel<name={self.name}, category={self.category.name}>"


class CellModel(models.Model):
    number = models.IntegerField(
        "Номер ячейки", unique=True,
        blank=True, null=True
    )

    count = models.IntegerField(
        "Количество", default=0
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

    def __str__(self) -> str:
        return f"Номер: {self.number}, Товар: {self.product.name}"

    def __repr__(self) -> str:
        return f"<CellModel number={self.number}, product={self.product.name}>"
