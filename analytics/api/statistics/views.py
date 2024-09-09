from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .sales.services import SaleService
from .sales.statistics import SalesStatistics
from .products.statistics import ProductStockStatistics
from .products.services import ProductStockService


@extend_schema_view(
    get=extend_schema(
        summary='Статистика продаж по категориям',
        description='Получение статистики продаж по категориям по всем автоматам',
        responses={
            status.HTTP_200_OK: {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "object",
                        "example": {
                            "Круассаны": 1,
                            "Пироги": 2
                        }
                    },
                    "total": {
                        "type": "number",
                        "example": 3
                    }
                }
            },
        },
        tags=["Статистика продаж"],
    )
)
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


@extend_schema_view(
    get=extend_schema(
        summary='Статистики продаж по товарам',
        description='Получение статистики продаж по товарам по всем автоматам',
        responses={
            status.HTTP_200_OK: {
                "type": "object",
                "properties": {
                    "product": {
                        "type": "object",
                        "example": {
                            "Классический круассан": 2,
                            "Гавайская пицца": 1
                        }
                    },
                    "total": {
                        "type": "number",
                        "example": 3
                    }
                }
            },
        },
        tags=["Статистика продаж"],
    )
)
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


@extend_schema_view(
    get=extend_schema(
        summary='Процент выкупа товара',
        description='Показывает процент, с которым человек оплачивает выбранный товар',
        tags=["Статистика продаж"],
    )
)
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


@extend_schema_view(
    get=extend_schema(
        summary="Выручка",
        description="Выручка по всем автоматам за все время",
        tags=["Статистика продаж"],
    )
)
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


@extend_schema_view(
    get=extend_schema(
        summary="Выручка за неделю",
        description="Выручка за последние 7 дней по всем автоматам",
        tags=["Статистика продаж"],
    )
)
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


@extend_schema_view(
    get=extend_schema(
        summary='Статистика по товарному остатку',
        description='Статистика по товарному остатку. Количество товара, которое осталось в каждом автомате',
        responses={
            status.HTTP_200_OK: serializers.AllProductStockSerializer(many=True)
        },
        tags=["Товарный остаток"],
    )
)
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
