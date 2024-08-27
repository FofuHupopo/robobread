from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import generics
from django.shortcuts import get_object_or_404

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
    
        return list(filter(lambda product: product.is_can_sell, queryset))


class AllProductListAPIView(generics.ListCreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


class CellListAPIView(generics.ListAPIView):
    queryset = models.CellModel.objects.all()
    serializer_class = serializers.CellSerializer


class CellDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = models.CellModel.objects.all()
    serializer_class = serializers.CellSerializer


class ProductInCellView(APIView):
    serializer_class = serializers.ProductInCellSerializer

    def get(self, request: Request, cell: int):
        product_in_cell = models.ProductInCellModel.objects.filter(
            cell_id=cell
        )

        serializer = self.serializer_class(
            product_in_cell,
            many=True
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def post(self, request: Request, cell: int):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save(cell_id=cell)

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )


class ProductInCellDetailView(APIView):
    serializer_class = serializers.ProductInCellSerializer

    def get_object(self, cell: int, pk: int):
        return get_object_or_404(
            models.ProductInCellModel,
            cell_id=cell, pk=pk
        )

    def get(self, request: Request, cell: int, pk: int):
        product_in_cell = self.get_object(cell, pk)

        serializer = self.serializer_class(product_in_cell)

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
    
    def put(self, request: Request, cell: int, pk: int):
        self.object = self.get_object(cell, pk)

        serializer = self.serializer_class(self.object, data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def delete(self, request: Request, cell: int, pk: int):
        product_in_cell = self.get_object(cell, pk)

        product_in_cell.delete()

        return Response({
            "message": "Товар удален из ячейки"
        }, status.HTTP_200_OK)
