from rest_framework import generics

from . import models
from . import serializers


class CategoryListView(generics.ListCreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if "category_id" not in self.kwargs:
            return queryset
        
        category_id = self.kwargs["category_id"]
        
        return queryset.filter(
            category_id=category_id
        )


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
