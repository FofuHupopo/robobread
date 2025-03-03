from rest_framework import serializers

from . import models


class RegisterMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MachineModel
        fields = ("sku", "name", "address")

    def create(self, validated_data):
        return models.MachineModel.objects.create(**validated_data)


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MachineModel
        fields = "__all__"


class MachineOrderSerializer(serializers.ModelSerializer):
    machine = MachineSerializer(read_only=True)

    class Meta:
        model = models.MachineOrderModel
        fields = "__all__"


class MachineCategorySerializer(serializers.ModelSerializer):
    machine = MachineSerializer(read_only=True)

    class Meta:
        model = models.MachineCategoryModel
        fields = "__all__"


class MachineProductSerializer(serializers.ModelSerializer):
    machine = MachineSerializer(read_only=True)

    class Meta:
        model = models.MachineProductModel
        fields = "__all__"


class MachineCellSerializer(serializers.ModelSerializer):
    machine = MachineSerializer(read_only=True)

    class Meta:
        model = models.MachineCellModel
        fields = "__all__"


class MachineProductInCellSerializer(serializers.ModelSerializer):
    machine = MachineSerializer(read_only=True)
    
    class Meta:
        model = models.MachineProductInCellModel
        fields = "__all__"
