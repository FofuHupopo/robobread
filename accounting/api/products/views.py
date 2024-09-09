from rest_framework import generics

from . import models
from . import serializers
from . import docs


@docs.category_list
class CategoryListView(generics.ListCreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@docs.category_detail
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@docs.product_list
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


@docs.product_detail
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

