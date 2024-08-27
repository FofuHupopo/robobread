from django.db import models
from django.utils import timezone


class VendingMachineModel(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    address = models.CharField(
        max_length=255,
        null=True, blank=True
    )
    name = models.CharField(
        max_length=100,
        null=True, blank=True
    )
    ip_address = models.CharField(
        max_length=100,
        unique=True
    )
    last_sync_date = models.DateTimeField(
        null=True, blank=True
    )
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES, default='active'
    )

    class Meta:
        db_table = 'core__vending_machines'
        verbose_name = "Автомат"
        verbose_name_plural = "Автоматы"

    def __str__(self):
        return f"{self.name} ({self.address})"

    def save(self, *args, **kwargs) -> None:
        if self.status == 'active':
            self.last_sync_date = timezone.now()

        return super().save(*args, **kwargs)
