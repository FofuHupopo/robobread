from django.contrib import admin

from . import models


admin.site.register(models.CategoryModel)
admin.site.register(models.ProductModel)
admin.site.register(models.CellModel)
