from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from . import serializers


sales_by_category = extend_schema_view(
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

sales_by_product = extend_schema_view(
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

percent_of_redemption = extend_schema_view(
    get=extend_schema(
        summary='Процент выкупа товара',
        description='Показывает процент, с которым человек оплачивает выбранный товар',
        tags=["Статистика продаж"],
    )
)

revenue = extend_schema_view(
    get=extend_schema(
        summary="Выручка",
        description="Выручка по всем автоматам за все время",
        tags=["Статистика продаж"],
    )
)

revenue_for_the_week = extend_schema_view(
    get=extend_schema(
        summary="Выручка за неделю",
        description="Выручка за последние 7 дней по всем автоматам",
        tags=["Статистика продаж"],
    )
)

all_product_stock = extend_schema_view(
    get=extend_schema(
        summary='Статистика по товарному остатку',
        description='Статистика по товарному остатку. Количество товара, которое осталось в каждом автомате',
        responses={
            status.HTTP_200_OK: serializers.AllProductStockSerializer(many=True)
        },
        tags=["Товарный остаток"],
    )
)
