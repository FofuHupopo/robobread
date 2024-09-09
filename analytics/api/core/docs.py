from rest_framework import serializers


class CreateVendingMachineSerializer(serializers.Serializer):
    ip_address = serializers.CharField()
