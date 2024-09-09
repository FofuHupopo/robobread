from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from . import models
from api.products import models as product_models
from . import serializers
from . import docs


@docs.order_list
class OrderListView(generics.ListCreateAPIView):
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


@docs.order_detail
class OrderDetailView(generics.RetrieveAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializer
