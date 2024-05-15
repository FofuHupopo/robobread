from django.db import models


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
        return super().__str__()


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

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        db_table = "products__products"
    
    def __str__(self) -> str:
        return f"ProductModel<name={self.name}, category={self.category.name}>"
