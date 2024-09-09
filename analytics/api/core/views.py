from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import permissions
from rest_framework import generics

from . import serializers
from . import models
from . import docs


@extend_schema_view(
    get=extend_schema(
        summary='Получение списка торговых автоматов',
        description='Получение списка торговых автоматов',
        tags=["Торговые автоматы"],
    ),
    post=extend_schema(
        summary='Создание торгового автомата',
        description='Создание торгового автомата',
        request=docs.CreateVendingMachineSerializer,
        tags=["Торговые автоматы"],
    )
)
class VendingMachinesListView(generics.ListCreateAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)


@extend_schema_view(
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
class VendingMachineDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
