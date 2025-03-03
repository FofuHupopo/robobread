from django.contrib import admin

from . import models


class ReadonlyAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(models.MachineModel, ReadonlyAdmin)
admin.site.register(models.MachineCategoryModel, ReadonlyAdmin)
admin.site.register(models.MachineCellModel, ReadonlyAdmin)
admin.site.register(models.MachineProductModel, ReadonlyAdmin)
admin.site.register(models.MachineProductInCellModel, ReadonlyAdmin)
admin.site.register(models.MachineOrderModel, ReadonlyAdmin)
