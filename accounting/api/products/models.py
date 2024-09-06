from typing import Type

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.utils import timezone


def category_image_upload_path(instance: models.Model, filename: str) -> str:
        return f"categories/{instance.pk}/{filename}"


class CategoryModel(models.Model):
    name = models.CharField(
        "Название", max_length=255
    )
    sku = models.CharField(
        "Артикул", max_length=128, unique=True
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


def product_image_upload_path(instance: models.Model, filename: str) -> str:
        return f"products/{instance.pk}/{filename}"


class ProductModel(models.Model):
    name = models.CharField(
        "Название", max_length=255,
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

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        db_table = "products__products"
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return f"ProductModel<name={self.name}, category={self.category.name}>"
