from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import serializers


class ProductBodyParamater(serializers.Serializer):
    product = serializers.IntegerField()


order_list = extend_schema_view(
    get=extend_schema(
        summary="Получение списка всех заказов",
        description="Получение списка всех заказов",
        tags=["Заказы"],
    ),
    post=extend_schema(
        summary="Создание заказа",
        description="Создание заказа. Первый этап оплаты (в поле product необходимо передать id товара)",
        request=ProductBodyParamater,
        tags=["Заказы"],
    )
)

order_detail = extend_schema_view(
    get=extend_schema(
        summary="Информация о заказе по id",
        description="Получение детальной информации по id заказа",
        tags=["Заказы"],
    )
)
