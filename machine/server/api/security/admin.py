from django.contrib import admin
from django.contrib.auth import models as auth_models

from . import models


admin.site.unregister(auth_models.User)
admin.site.unregister(auth_models.Group)

admin.site.register(models.SynchronizerTokenModel)
