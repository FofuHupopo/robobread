import uuid

from django.db import models


class SynchronizerTokenModel(models.Model):
    token = models.UUIDField("Токен", default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        verbose_name = "Токен сервиса синхронизации"
        verbose_name_plural = "Токены сервиса синхронизации"

    def __str__(self):
        return str(self.token)
