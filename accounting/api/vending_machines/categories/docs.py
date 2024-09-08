from rest_framework import serializers


class CategoryRequestSerializer(serializers.Serializer):
    category_sku = serializers.CharField()
