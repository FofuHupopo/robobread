from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer

from .data import ProductsInCellData, CellData
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


class CellSerializer(DataclassSerializer):
    product = VendingMachineProductSerializer()

    class Meta:
        dataclass = CellData
        fields = "__all__"
        depth = 2


class ProductsInCellSerializer(DataclassSerializer):
    cells = CellSerializer(many=True)

    class Meta:
        dataclass = ProductsInCellData
        fields = ("cells", )
        depth = 2
