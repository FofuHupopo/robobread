from django.contrib import admin

from . import models


admin.site.register((
    models.SalesModel,
    models.ProductStockModel
))
