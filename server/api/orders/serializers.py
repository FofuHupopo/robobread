from rest_framework import serializers

from api.products.serializers import ProductWithOutCellsSerializer
from . import models


class OrderSerializer(serializers.ModelSerializer):
    product = ProductWithOutCellsSerializer()

    class Meta:
        model = models.OrderModel
        fields = '__all__'
        depth = 2
