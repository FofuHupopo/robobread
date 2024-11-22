from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer

from .data import ProductInCellData, CellDetailData, CellData, CreateCellData, UpdateCellData
from api.vending_machines.vending_machines.serializers import VendingMachineDataSerializer
from api.vending_machines.categories.serializers import VendingMachineCategorySerializer


class ProductInCellDataSerializer(DataclassSerializer):
    class Meta:
        dataclass = ProductInCellData
        fields = "__all__"


class CellDetailDataSerializer(DataclassSerializer):
    products = ProductInCellDataSerializer(many=True)

    class Meta:
        dataclass = CellDetailData
        fields = "__all__"
        depth = 1


class CellDataSerializer(VendingMachineDataSerializer):
    cells = CellDetailDataSerializer(many=True)

    class Meta:
        dataclass = CellData
        fields = "__all__"
        depth = 2


class CreateCellDataSerializer(DataclassSerializer):
    class Meta:
        dataclass = CreateCellData
        fields = "__all__"


class UpdateCellDataSerializer(DataclassSerializer):
    class Meta:
        dataclass = UpdateCellData
        fields = "__all__"
