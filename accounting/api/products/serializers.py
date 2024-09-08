from rest_framework import serializers

from . import models


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
