from rest_framework import serializers

from . import models
from api.products.serializers import ProductSerializer
from api.vending_machines.serializers import VendingMachineSerializer


class PackingAddedItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField()

    class Meta:
        model = models.PackingAddedItemModel
        fields = "__all__"
        depth = 1


class PackingRemovedItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField()

    class Meta:
        model = models.PackingRemovedItemModel
        fields = "__all__"
        depth = 1


class PackingSerializer(serializers.ModelSerializer):
    added_items = PackingAddedItemSerializer(many=True)
    removed_items = PackingAddedItemSerializer(many=True)
    vending_machine = VendingMachineSerializer(read_only=True)
    vending_machine_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = models.PackingModel
        fields = "__all__"
        depth = 2

    def create(self, validated_data):
        added_items_data = validated_data.pop('added_items')
        removed_items_data = validated_data.pop('removed_items')

        packing = models.PackingModel.objects.create(**validated_data)

        for added_item_data in added_items_data:
            models.PackingAddedItemModel.objects.create(
                packing=packing,
                **added_item_data
            )

        for removed_item_data in removed_items_data:
            models.PackingRemovedItemModel.objects.create(
                packing=packing,
                **removed_item_data
            )

        return packing

    def update(self, instance, validated_data):
        for added_item_data in validated_data.pop('added_items'):
            added_item_instance = models.PackingAddedItemModel.objects.get(
                id=added_item_data.pop('id')
            )

            for key, value in added_item_data.items():
                setattr(added_item_instance, key, value)

            added_item_instance.save()

        for removed_item_data in validated_data.pop('removed_items'):
            removed_item_instance = models.PackingAddedItemModel.objects.get(
                id=removed_item_data.pop('id')
            )

            for key, value in removed_item_instance.items():
                setattr(removed_item_instance, key, value)

            removed_item_instance.save()

        return super().update(instance, validated_data)
