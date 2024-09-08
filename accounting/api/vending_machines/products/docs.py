from rest_framework import serializers


class ProductRequestSerializer(serializers.Serializer):
    product_sku = serializers.CharField()
