from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer

from . import models
from api.vending_machines.serializers import VendingMachineDataSerializer
from . import data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)
    category_id = serializers.IntegerField(write_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = models.ProductModel
        fields = "__all__"
        depth = 1


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
        dataclass = data.CategoryData
        depth = 1


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
