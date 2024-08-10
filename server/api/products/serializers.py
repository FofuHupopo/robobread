from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = '__all__'


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CellModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        depth = 1
        fields = (
            'id', 'name', 'description',
            'composition', 'price', 'image',
            'category', 'cells',
        )
