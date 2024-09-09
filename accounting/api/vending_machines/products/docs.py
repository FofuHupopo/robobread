from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import serializers
from rest_framework import status

from .serializers import ProductDataSerializer


class ProductRequestSerializer(serializers.Serializer):
    product_sku = serializers.CharField()


vending_machine_product_list = extend_schema_view(
    get=extend_schema(
        summary="Получение списка продуктов в автомате",
        description="Получение списка продуктов в автомате",
        responses={
            status.HTTP_200_OK: ProductDataSerializer
        },
        tags=["Товары автомата"],
    ),
    post=extend_schema(
        summary="Добавление продукта в список автомата",
        description="Добавление продукта в список автомата",
        request=ProductRequestSerializer,
        responses={
            status.HTTP_201_CREATED: ProductDataSerializer
        },
        tags=["Товары автомата"],
    ),
    delete=extend_schema(
        summary="Удаление продукта из списка автомата",
        description="Удаление продукта из списка автомата",
        parameters=[
            OpenApiParameter(
                name='product_sku',
                location=OpenApiParameter.QUERY,
                description='ID продукта',
                type=OpenApiTypes.INT,
                required=True
            )
        ],
        responses={
            status.HTTP_200_OK: ProductDataSerializer
        },
        tags=["Товары автомата"],
    ),
    put=extend_schema(
        summary="Обновление продукта в списке автомата",
        description="Обновление продукта в списке автомата",
        request=ProductRequestSerializer,
        responses={
            status.HTTP_200_OK: ProductDataSerializer
        },
        tags=["Товары автомата"],
    )
)