from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework import permissions

from . import serializers
from . import models


@extend_schema_view(
    get=extend_schema(
        summary="Получение списка автоматов",
        description="Возвращает список автоматов",
        tags=["Торговые автоматы"],
    ),
    post=extend_schema(
        summary="Создание автомата",
        description="Создает автомат",
        tags=["Торговые автоматы"],
    ),
)
class VendingMachineListView(generics.ListCreateAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)


@extend_schema_view(
    get=extend_schema(
        summary="Получение автомата по id",
        description="Возвращает автомат по id",
        tags=["Торговые автоматы"],
    ),
    put=extend_schema(
        summary="Обновление автомата",
        description="Обновляет автомат",
        tags=["Торговые автоматы"],
    ),
    patch=extend_schema(
        summary="Обновление автомата",
        description="Обновляет автомат",
        tags=["Торговые автоматы"],
    ),
    delete=extend_schema(
        summary="Удаление автомата",
        description="Удаляет автомат",
        tags=["Торговые автоматы"],
    ),
)
class VendingMachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)
