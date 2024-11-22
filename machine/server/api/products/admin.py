from django.contrib import admin

from . import models


class ProductInline(admin.TabularInline):
    model = models.ProductModel
    extra = 1


@admin.register(models.CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline] 


@admin.register(models.ProductModel)
class ProductAdmin(admin.ModelAdmin):
    model = models.ProductModel
    list_filter = ('category',)


@admin.register(models.CellModel)
class CellAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'count', )

admin.site.register(models.ProductInCellModel)
