from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics

from . import models
from . import serializers


@extend_schema_view(
    get=extend_schema(
        summary='Получение списка категорий',
        description='Получение списка категорий',
        tags=['Категории'],
    ),
    post=extend_schema(
        summary='Создание категории',
        description='Создание категории',
        tags=['Категории'],
    ),
)
class CategoryListView(generics.ListCreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@extend_schema_view(
    get=extend_schema(
        summary='Получение категории',
        description='Получение категории',
        tags=['Категории'],
    ),
    put=extend_schema(
        summary='Обновление категории',
        description='Обновление категории',
        tags=['Категории'],
    ),
    patch=extend_schema(
        summary='Обновление категории',
        description='Обновление категории',
        tags=['Категории'],
    ),
    delete=extend_schema(
        summary='Удаление категории',
        description='Удаление категории',
        tags=['Категории'],
    )
)
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@extend_schema_view(
    get=extend_schema(
        summary='Получение списка товаров',
        description='Получение списка товаров',
        parameters=[
            OpenApiParameter(
                name='category_id',
                location=OpenApiParameter.QUERY,
                description='ID категории',
                type=OpenApiTypes.INT
            )
        ],
        tags=['Товары'],
    ),
    post=extend_schema(
        summary='Создание товара',
        description='Создание товара',
        tags=['Товары'],
    )
)
class ProductListView(generics.ListCreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        query_params = self.request.query_params

        if "category_id" not in query_params:
            return queryset
        
        category_id = query_params["category_id"]
        
        return queryset.filter(
            category_id=category_id
        )


@extend_schema_view(
    get=extend_schema(
        summary='Получение товара',
        description='Получение товара',
        tags=['Товары'],
    ),
    put=extend_schema(
        summary='Обновление товара',
        description='Обновление товара',
        tags=['Товары'],
    ),
    patch=extend_schema(
        summary='Обновление товара',
        description='Обновление товара',
        tags=['Товары'],
    ),
    delete=extend_schema(
        summary='Удаление товара',
        description='Удаление товара',
        tags=['Товары'],
    )
)
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

