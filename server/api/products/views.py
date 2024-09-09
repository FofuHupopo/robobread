from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404

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
class ProductListView(generics.ListAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        category_id = self.request.query_params.get('category_id', None)

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return list(filter(lambda product: product.is_can_sell, queryset))


@docs.all_product_list
class AllProductListView(generics.ListCreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


@docs.product_detail
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


@docs.cell_list
class CellListView(generics.ListCreateAPIView):
    queryset = models.CellModel.objects.all()
    serializer_class = serializers.CellSerializer


@docs.cell_detail
class CellDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CellModel.objects.all()
    serializer_class = serializers.CellSerializer

    def delete(self, request, *args, **kwargs):
        if self.get_object().count > 0:
            return Response(
                {"message": "Нельзя удалить непустую ячейку с товароми"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().delete(request, *args, **kwargs)


@docs.product_in_cell
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


@docs.product_in_cell_detail
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


@docs.packing
class PackingView(APIView):
    serializer_class = serializers.PackingSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data, many=True)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        packing_result = serializer.create(serializer.validated_data)

        serializer = serializers.PackingResultSerializer(packing_result)

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
