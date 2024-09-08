from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema

from . import models
from . import serializers

@extend_schema_view(
    get=extend_schema(
        summary="Получение списка операций затаривания",
        description="Возвращает список операций затаривания",
        tags=["Затаривание"],
    ),
    post=extend_schema(
        summary="Создание операции затаривания",
        description="Создает операцию затаривания",
        tags=["Затаривание"],
    ),
)
class PackingView(generics.ListCreateAPIView):
    queryset = models.PackingModel.objects.all()
    serializer_class = serializers.PackingSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Получение операции затаривания",
        description="Возвращает операцию затаривания",
        tags=["Затаривание"],
    ),
    put=extend_schema(
        summary="Обновление операции затаривания",
        description="Обновляет операцию затаривания",
        tags=["Затаривание"],
    ),
    patch=extend_schema(
        summary="Обновление операции затаривания",
        description="Обновляет операцию затаривания",
        tags=["Затаривание"],
    ),
    delete=extend_schema(
        summary="Удаление операции затаривания",
        description="Удаляет операцию затаривания",
        tags=["Затаривание"],
    ),
)
class PackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PackingModel.objects.all()
    serializer_class = serializers.PackingSerializer
