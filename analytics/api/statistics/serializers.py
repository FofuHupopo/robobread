from rest_framework import serializers
from rest_framework_dataclasses.serializers import DataclassSerializer


from api.core.serializers import VendingMachineSerializer
from . import models
from api.statistics.sales.services import SaleData
from api.statistics.products.services import ProductData


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SalesModel
        fields = "__all__"


class ProductStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductStockModel
        fields = "__all__"


class SaleSerializer(DataclassSerializer):
    vending_machine = VendingMachineSerializer()
    sales = SalesSerializer(many=True)

    class Meta:
        dataclass = SaleData
        depth = 1


class ProductSerializer(DataclassSerializer):
    vending_machine = VendingMachineSerializer()
    product_stock = ProductStockSerializer(many=True)

    class Meta:
        dataclass = ProductData
        depth = 1


class SaleByCategorySerializer(serializers.Serializer):
    category = serializers.DictField(child=serializers.IntegerField())
    total = serializers.IntegerField()


class SaleByProductSerializer(serializers.Serializer):
    product = serializers.DictField(child=serializers.IntegerField())
    total = serializers.IntegerField()


class PercentOfRedemptionSerializer(serializers.Serializer):
    percent = serializers.FloatField()


class RevenueSerializer(serializers.Serializer):
    revenue = serializers.FloatField()


class RevenueForTheWeekSerializer(serializers.Serializer):
    revenue_for_the_week = serializers.ListField(child=serializers.IntegerField(), max_length=7, min_length=7)
    total = serializers.IntegerField()


class AllProductStockSerializer(serializers.Serializer):
    product_stock = ProductStockSerializer(many=True)
    vending_machine = VendingMachineSerializer()
