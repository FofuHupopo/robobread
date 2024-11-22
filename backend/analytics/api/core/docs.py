from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import serializers


class CreateVendingMachineSerializer(serializers.Serializer):
    ip_address = serializers.CharField()


vending_machines_list = extend_schema_view(
    get=extend_schema(
        summary='Получение списка торговых автоматов',
        description='Получение списка торговых автоматов',
        tags=["Торговые автоматы"],
    ),
    post=extend_schema(
        summary='Создание торгового автомата',
        description='Создание торгового автомата',
        request=CreateVendingMachineSerializer,
        tags=["Торговые автоматы"],
    )
)

vending_machine_detail = extend_schema_view(
    get=extend_schema(
        summary='Получение торгового автомата',
        description='Получение торгового автомата',
        tags=["Торговые автоматы"],
    ),
    delete=extend_schema(
        summary='Удаление торгового автомата',
        description='Удаление торгового автомата',
        tags=["Торговые автоматы"],
    )
)
