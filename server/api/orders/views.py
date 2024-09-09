from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from . import models
from api.products import models as product_models
from . import serializers
from . import docs


@extend_schema_view(
    get=extend_schema(
        summary="Получение списка всех заказов",
        description="Получение списка всех заказов",
        tags=["Заказы"],
    ),
    post=extend_schema(
        summary="Создание заказа",
        description="Создание заказа. Первый этап оплаты (в поле product необходимо передать id товара)",
        request=docs.ProductBodyParamater,
        tags=["Заказы"],
    )
)
class OrderListAPIView(generics.ListCreateAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializer
    
    def post(self, request: Request, *args, **kwargs):
        product_id = request.data.get('product')
        
        try:
            product = product_models.ProductModel.objects.get(id=product_id)
        except product_models.ProductModel.DoesNotExist:
            return Response({
                "status": f"Не был найден товар с {product_id=}."
            }, status.HTTP_400_BAD_REQUEST)
        
        order = models.OrderModel.objects.create(
            product=product,
            amount=product.price
        )

        serializer = self.serializer_class(order)
            
        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )


@extend_schema_view(
    get=extend_schema(
        summary="Информация о заказе по id",
        description="Получение детальной информации по id заказа",
        tags=["Заказы"],
    )
)
class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializer
