from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import serializers
from rest_framework import status

from .serializers import CategoryDataSerializer


class CategoryRequestSerializer(serializers.Serializer):
    category_sku = serializers.CharField()


vending_machine_category_list = extend_schema_view(
    get=extend_schema(
        summary="Получение списка категорий в автомате",
        description="Получение списка категорий в автомате",
        responses={
            status.HTTP_200_OK: CategoryDataSerializer
        },
        tags=["Категории автомата"],
    ),
    post=extend_schema(
        summary="Добавление категории в список автомата",
        description="Добавление категории в список автомата",
        request=CategoryRequestSerializer,
        responses={
            status.HTTP_201_CREATED: CategoryDataSerializer
        },
        tags=["Категории автомата"],
    ),
    delete=extend_schema(
        summary="Удаление категории из списка автомата",
        description="Удаление категории из списка автомата",
        parameters=[
            OpenApiParameter(
                name='category_sku',
                location=OpenApiParameter.QUERY,
                description='ID категории',
                type=OpenApiTypes.INT,
                required=True
            )
        ],
        responses={
            status.HTTP_200_OK: CategoryDataSerializer
        },
        tags=["Категории автомата"],
    ),
    put=extend_schema(
        summary="Обновление категории в списке автомата",
        description="Обновление категории в списке автомата",
        request=CategoryRequestSerializer,
        responses={
            status.HTTP_200_OK: CategoryDataSerializer
        },
        tags=["Категории автомата"],
    )
)
