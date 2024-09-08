from rest_framework import serializers


class CellIdInRequestSerializer(serializers.Serializer):
    cell_id = serializers.IntegerField()
