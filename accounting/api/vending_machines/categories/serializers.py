from rest_framework import serializers

from .data import CategoryData
from api.vending_machines.vending_machines.serializers import VendingMachineDataSerializer


class VendingMachineCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    sku = serializers.CharField()
    image = serializers.CharField()

    class Meta:
        fields = ("id", "name", "sku", "image")
        depth = 1


class CategoryDataSerializer(VendingMachineDataSerializer):
    categories = VendingMachineCategorySerializer(many=True)

    class Meta:
        dataclass = CategoryData
        depth = 1
