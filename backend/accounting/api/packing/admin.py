from django.contrib import admin

from . import models


admin.site.register((
    models.PackingModel,
    models.PackingAddedItemModel,
    models.PackingRemovedItemModel
))
