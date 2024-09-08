from django.db import IntegrityError
from rest_framework import serializers

from collections import defaultdict

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
        fields = "__all__"


class ProductWithOutCellsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = (
            'id', 'name', 'description', 'sku', 'composition',
            'expiration_date', 'price', 'image',
            'category',
        )


class CellSerializer(serializers.ModelSerializer):
    products = ProductInCellSerializer(many=True, read_only=True)
    product = ProductWithOutCellsSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.CellModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    cells = CellSerializer(many=True, read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.ProductModel
        depth = 2
        fields = (
            'id', 'name', 'description', 'sku', 'composition',
            'expiration_date', 'price', 'image',
            'category', 'category_id', 'cells',
        )


class PackingSerializer(serializers.Serializer):
    cell = serializers.IntegerField()
    count = serializers.IntegerField()
    removed = serializers.IntegerField()

    class Meta:
        fields = ('cell', 'count', 'removed')

    def validate_cell(self, cell_id):
        try:
            cell = models.CellModel.objects.get(
                id=cell_id
            )
            return cell

        except models.CellModel.DoesNotExist:
            raise serializers.ValidationError('Cell not found')

    def create(self, validated_data):
        cell: models.CellModel = validated_data.get("cell")
        count: int = validated_data.get("count")
        removed: int = validated_data.get("removed")
        added = count - removed - cell.count

        for _ in range(removed):
            cell.remove_product()
        
        if added >= 0:
            for _ in range(added):
                cell.add_product()
        else:
            for _ in range(-added):
                cell.remove_product()

        return {
            "product_id": cell.product.pk,
            "removed": removed,
            "added": added
        }


class PackingResultItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    count = serializers.IntegerField()


class PackingResultSerializer(serializers.Serializer):
    added_items = PackingResultItemSerializer(many=True)
    removed_items = PackingResultItemSerializer(many=True)

    def to_representation(self, instance):
        added_counts = defaultdict(int)
        removed_counts = defaultdict(int)

        for item in instance:
            product_id = item['product_id']
            added_counts[product_id] += item['added']
            removed_counts[product_id] += item['removed']

        added_items = []
        removed_items = []

        for product_id, count in added_counts.items():
            if count > 0:
                added_items.append({'product_id': product_id, 'count': count})

        for product_id, count in removed_counts.items():
            if count > 0:
                removed_items.append({'product_id': product_id, 'count': count})

        return {
            'added_items': added_items,
            'removed_items': removed_items,
        }
