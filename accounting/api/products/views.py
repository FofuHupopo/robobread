from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics

from . import models
from . import serializers


@extend_schema_view(
    get=extend_schema(
        summary='Получение списка категорий',
        description='Получение списка категорий',
    ),
    post=extend_schema(
        summary='Создание категории',
        description='Создание категории',
    )
)
class CategoryListView(generics.ListCreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@extend_schema_view(
    get=extend_schema(
        summary='Получение категории',
        description='Получение категории'
    ),
    put=extend_schema(
        summary='Обновление категории',
        description='Обновление категории',
    ),
    patch=extend_schema(
        summary='Обновление категории',
        description='Обновление категории',
    ),
    delete=extend_schema(
        summary='Удаление категории',
        description='Удаление категории'
    )
)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@extend_schema_view(
    get=extend_schema(
        summary='Получение списка продуктов',
        description='Получение списка продуктов',
        parameters=[
            OpenApiParameter(
                name='category_id',
                location=OpenApiParameter.QUERY,
                description='ID категории',
                type=OpenApiTypes.INT
            )
        ]
    ),
    post=extend_schema(
        summary='Создание продукта',
        description='Создание продукта'
    )
)
class ProductListView(generics.ListCreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        query_params =self.request.query_params

        if "category_id" not in query_params:
            return queryset
        
        category_id = query_params["category_id"]
        
        return queryset.filter(
            category_id=category_id
        )


@extend_schema_view(
    get=extend_schema(
        summary='Получение продукта',
        description='Получение продукта',
    ),
    put=extend_schema(
        summary='Обновление продукта',
        description='Обновление продукта',
    ),
    patch=extend_schema(
        summary='Обновление продукта',
        description='Обновление продукта',
    ),
    delete=extend_schema(
        summary='Удаление продукта',
        description='Удаление продукта',
    )
)
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

