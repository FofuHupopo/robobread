from rest_framework import generics
from drf_spectacular.utils import extend_schema, extend_schema_view

from . import models
from . import serializers
from . import docs


@extend_schema_view(
    post=extend_schema(
        request=docs.ProductBodyParamater
    )
)
class OrderListAPIView(generics.ListCreateAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializer
