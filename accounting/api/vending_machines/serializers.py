from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer

from . import models
from . import data


class VendingMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VendingMachineModel
        fields = "__all__"


class VendingMachineDataSerializer(DataclassSerializer):
    vending_machine = VendingMachineSerializer()

    class Meta:
        dataclass = data.VendingMachineData
        depth = 1
