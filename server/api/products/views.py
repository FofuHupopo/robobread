from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import generics
from django.shortcuts import get_object_or_404

from . import models
from . import serializers


@extend_schema_view(
    get=extend_schema(
        summary="Список категорий",
        description="Получение списка категорий",
        tags=["Категории"],
    ),
    post=extend_schema(
        summary="Создание категории",
        description="Создание категории",
        tags=["Категории"],
    )
)
class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@extend_schema_view(
    get=extend_schema(
        summary="Информация о категории",
        description="Получение детальной информации по id категории",
        tags=["Категории"],
    ),
    put=extend_schema(
        summary="Изменение категории",
        description="Изменение информации категории по id",
        tags=["Категории"],
    ),
    patch=extend_schema(
        summary="Изменение категории",
        description="Изменение информации категории по id",
        tags=["Категории"],
    ),
    delete=extend_schema(
        summary="Удаление категории",
        description="Удаление категории по id",
        tags=["Категории"],
    ),
)
class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer


@extend_schema_view(
    get=extend_schema(
        summary="Список товаров по категориям",
        description="Если указать category_id в query параметрах, то вернет только товары этой категории",
        parameters=[
            OpenApiParameter(
                name="category_id",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
                required=False
            ),
        ],
        tags=["Товары"],
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


@extend_schema_view(
    get=extend_schema(
        summary="Список всех товаров",
        description="Получение списка всех товаров",
        tags=["Товары"],
    ),
    post=extend_schema(
        summary="Создание товара",
        description="Создание товара",
        tags=["Товары"],
    )
)
class AllProductListAPIView(generics.ListCreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Информация о товаре",
        description="Получение детальной информации по id товара",
        tags=["Товары"],
    ),
    put=extend_schema(
        summary="Изменение товара",
        description="Изменение информации о товаре по id",
        tags=["Товары"],
    ),
    patch=extend_schema(
        summary="Изменение товара",
        description="Изменение информации о товаре по id",
        tags=["Товары"],
    ),
    delete=extend_schema(
        summary="Удаление товара",
        description="Удаление товара по id",
        tags=["Товары"],
    ),
)
class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Список ячеек",
        description="Получение списка ячеек",
        tags=["Ячейки"],
    ),
    post=extend_schema(
        summary="Создание ячейки",
        description="Создание ячейки",
        tags=["Ячейки"],
    )
)
class CellListAPIView(generics.ListCreateAPIView):
    queryset = models.CellModel.objects.all()
    serializer_class = serializers.CellSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Информация о ячейке",
        description="Получение детальной информации по id ячейки",
        tags=["Ячейки"],
    ),
    put=extend_schema(
        summary="Изменение ячейки",
        description="Изменение информации ячейки по id",
        tags=["Ячейки"],
    ),
    patch=extend_schema(
        summary="Изменение ячейки",
        description="Изменение информации ячейки по id",
        tags=["Ячейки"],
    ),
    delete=extend_schema(
        summary="Удаление ячейки",
        description="Удаление ячейки по id",
        tags=["Ячейки"],
    ),
)
class CellDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CellModel.objects.all()
    serializer_class = serializers.CellSerializer

    def delete(self, request, *args, **kwargs):
        if self.get_object().count > 0:
            return Response(
                {"message": "Нельзя удалить непустую ячейку с товароми"},
                status=status.HTTP_403_FORBIDDEN
            )

        return super().delete(request, *args, **kwargs)


@extend_schema_view(
    get=extend_schema(
        summary="Список товаров в ячейке",
        description="Получение списка товаров в ячейке",
        tags=["Товар в ячейке"],
    ),
    post=extend_schema(
        summary="Добавление товара в ячейку",
        description="Добавление товара в ячейку",
        tags=["Товар в ячейке"],
    )
)
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


@extend_schema_view(
    get=extend_schema(
        summary="Информация о товаре в ячейке",
        description="Получение детальной информации о товаре в ячейке",
        tags=["Товар в ячейке"],
    ),
    put=extend_schema(
        summary="Изменение товаре в ячейке",
        description="Изменение информации о товаре в ячейке",
        tags=["Товар в ячейке"],
    ),
    delete=extend_schema(
        summary="Удаление товара из ячейки",
        description="Удаление товара из ячейки",
        tags=["Товар в ячейке"],
    )
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


@extend_schema_view(
    post=extend_schema(
        summary="Затаривание",
        description="Создание нового затаривания",
        request=serializers.PackingSerializer,
        responses={
            status.HTTP_201_CREATED: serializers.PackingResultSerializer
        },
        tags=["Затаривание"]
    )
)
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
