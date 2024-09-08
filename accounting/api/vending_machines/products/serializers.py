from rest_framework import serializers

from . import data
from api.vending_machines.vending_machines.serializers import VendingMachineDataSerializer
from api.vending_machines.categories.serializers import VendingMachineCategorySerializer


class VendingMachineProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    composition = serializers.CharField()
    sku = serializers.CharField()
    category = VendingMachineCategorySerializer()
    expiration_date = serializers.CharField()
    price = serializers.IntegerField()
    image = serializers.CharField()

    class Meta:
        fields = (
            "id", "name", "description", "composition", "sku",
            "category", "expiration_date", "price", "image"
        )
        depth = 1


class ProductDataSerializer(VendingMachineDataSerializer):
    products = VendingMachineProductSerializer(many=True)

    class Meta:
        dataclass = data.ProductData
        depth = 1
