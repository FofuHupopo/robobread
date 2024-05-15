from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import generics

from . import models
from . import serializers


class CategoryListAPIView(generics.ListAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@extend_schema_view(
    get=extend_schema(
        description="Если указать category_id в query параметрах, то вернет только товары этой категории",
        parameters=[
            OpenApiParameter("category_id", OpenApiTypes.STR, required=False),
        ]
    )
)
class ProductListAPIView(generics.ListAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        category_id = self.request.query_params.get('category_id', None)
        
        if category_id:
            queryset = queryset.filter(category_id=category_id)
            
        return queryset


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
