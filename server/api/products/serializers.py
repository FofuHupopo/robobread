from rest_framework import serializers

from . import models


class ProductInCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductInCellModel
        fields = (
            "id", "upload_date", "expiration_date",
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = '__all__'


class CellSerializer(serializers.ModelSerializer):
    products = ProductInCellSerializer(many=True)

    class Meta:
        model = models.CellModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    cells = CellSerializer(many=True)

    class Meta:
        model = models.ProductModel
        depth = 2
        fields = (
            'id', 'name', 'description',
            'composition', 'price', 'image',
            'category', 'cells',
        )
