from rest_framework import serializers


class ProductBodyParamater(serializers.Serializer):
    product = serializers.IntegerField()
