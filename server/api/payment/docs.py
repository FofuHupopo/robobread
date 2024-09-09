from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiTypes
from rest_framework import status
from rest_framework import serializers


class OrderIdBodyParamater(serializers.Serializer):
    order_id = serializers.UUIDField()
    

class PaymentIdBodyParamater(serializers.Serializer):
    payment_id = serializers.UUIDField()


payment = extend_schema_view(
    get=extend_schema(
        summary="Получение информации по оплате",
        description="Получение информации по оплате, по payment_id из query параметров",
        parameters=[
            OpenApiParameter("payment_id", OpenApiTypes.STR)
        ],
        tags=["Оплата"],
    ),
    post=extend_schema(
        summary="Создание оплаты",
        description="Второй этап оплаты. В поле order_id необходимо передать id заказа",
        request=OrderIdBodyParamater,
        tags=["Оплата"],
    )
)

qr_payment = extend_schema_view(
    get=extend_schema(
        summary="Получение QR кода оплаты",
        description="Получение QR кода в формате <svg>, который необходимо отобразить на странице оплаты. Третий этап оплаты",
        parameters=[
            OpenApiParameter(
                name="payment_id",
                type=OpenApiTypes.STR
            )
        ],
        responses={
            status.HTTP_200_OK: OpenApiTypes.STR
        },
        tags=["Оплата"],
    )
)

cancel_payment = extend_schema_view(
    get=extend_schema(
        summary="Отмена оплаты",
        description="Отмена оплаты на стороне Тинькофф. Интрефейса на автомате нет",
        parameters=[
            OpenApiParameter(
                name="payment_id",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
            )
        ],
        tags=["Оплата"],
    )
)

sbp_pay_test = extend_schema_view(
    get=extend_schema(
        summary="Тестовая оплаты по sbp",
        description="Проведение тестовой оплаты через sbp, необходимо для тестирования",
        parameters=[
            OpenApiParameter(
                name="payment_id",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="is_expired",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.BOOL,
                default=False,
                required=False
            ),
            OpenApiParameter(
                name="is_rejected",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.BOOL,
                default=False,
                required=False
            )
        ],
        tags=["Оплата"],
    )
)
