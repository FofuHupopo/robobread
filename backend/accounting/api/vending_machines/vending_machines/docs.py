from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status

from . import serializers


sync_one_vending_machine = extend_schema_view(
    get=extend_schema(
        summary="Синхронизация данных для одного аппарата",
        description="Синхронизация данных для одного аппарата",
        responses={
            status.HTTP_200_OK: serializers.VendingMachineDataSerializer
        },
        tags=["Синхронизация"],
    )
)

sync_vending_machines = extend_schema_view(
    get=extend_schema(
        summary="Синхронизация данных для всех аппаратов",
        description="Синхронизация данных для всех аппаратов",
        responses={
            status.HTTP_200_OK: serializers.VendingMachineDataSerializer(many=True)
        },
        tags=["Синхронизация"],
    )
)
