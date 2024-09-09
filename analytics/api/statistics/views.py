from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import docs
from .sales.services import SaleService
from .sales.statistics import SalesStatistics
from .products.statistics import ProductStockStatistics
from .products.services import ProductStockService


@docs.sales_by_category
class SalesByCategoryView(APIView):
    serializer_class = serializers.SaleByCategorySerializer

    def get(self, request: Request):
        serializer = self.serializer_class(
            SalesStatistics(
                SaleService.get_syncronized_vending_machines()
            ).by_category()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


@docs.sales_by_product
class SalesByProductView(APIView):
    serializer_class = serializers.SaleByProductSerializer

    def get(self, request: Request):
        serializer = self.serializer_class(
            SalesStatistics(
                SaleService.get_syncronized_vending_machines()
            ).by_product()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


@docs.percent_of_redemption
class PercentOfRedemptionView(APIView):
    serializer_class = serializers.PercentOfRedemptionSerializer

    def get(self, request: Request):
        serializer = self.serializer_class(
            SalesStatistics(
                SaleService.get_syncronized_vending_machines()
            ).percent_of_redemption()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


@docs.revenue
class RevenueView(APIView):
    serializer_class = serializers.RevenueSerializer

    def get(self, request: Request):
        serializer = self.serializer_class(
            SalesStatistics(
                SaleService.get_syncronized_vending_machines()
            ).revenue()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


@docs.revenue_for_the_week
class RevenueForTheWeekView(APIView):
    serializer_class = serializers.RevenueForTheWeekSerializer

    def get(self, request: Request):
        serializer = self.serializer_class(
            SalesStatistics(
                SaleService.get_syncronized_vending_machines()
            ).revenue_for_the_week()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


@docs.all_product_stock
class AllProductStockView(APIView):
    serializer_class = serializers.AllProductStockSerializer

    def get(self, request: Request):
        serializer = self.serializer_class(
            ProductStockStatistics(
                ProductStockService.get_syncronized_vending_machines()
            ).product_stock(),
            many=True
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
