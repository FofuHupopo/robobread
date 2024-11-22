from rest_framework import serializers

from . import models


class VendingMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VendingMachineModel
        fields = "__all__"
