import os
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework.renderers import StaticHTMLRenderer
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiTypes

from api.utils import InteractionCommand
from api.orders import models as orders_models
from .services import MerchantAPI
from . import models
from . import docs
from . import serializers


merchant_api = MerchantAPI(
    terminal_key=os.getenv("TERMINAL_KEY"),
    secret_key=os.getenv("SECRET_KEY"),
)


@extend_schema_view(
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
        request=docs.OrderIdBodyParamater,
        tags=["Оплата"],
    )
)
class PaymentView(APIView):
    serializer_class = serializers.PaymentSerializer
    permission_classes = [AllowAny]

    def get(self, request: Request):
        payment_id = request.query_params.get("payment_id")
        
        if not payment_id:
            return Response({
                "status": "Не передан payment_id."
            }, status.HTTP_400_BAD_REQUEST)

        try:
            payment = models.PaymentModel.objects.get(
                id=payment_id
            )
        except models.PaymentModel.DoesNotExist:
            return Response({
                "status": f"Не была найдена оплата с {payment_id=}."
            }, status.HTTP_400_BAD_REQUEST)
            
        payment_is_paid_old = payment.is_paid()

        merchant_api.status(payment)
        payment.save()
        
        payment_is_paid_new = payment.is_paid()
        
        if payment_is_paid_old == False and payment_is_paid_new == True:
            order = orders_models.OrderModel.objects.get(pk=payment.order_id)
            product = order.product
            
            if not product.is_empty:
                cell = product.get_first_available_cell()

                InteractionCommand().sell_item(cell.number)

                cell.count -= 1
                cell.save()

        if payment.is_paid():
            order = orders_models.OrderModel.objects.get(
                pk=payment.order_id
            )

            order.paid()

        serializer = self.serializer_class(payment)

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def post(self, request: Request):
        order_id = request.data.get("order_id")

        if not order_id:
            return Response({
                "status": "Не передан order_id."
            }, status.HTTP_400_BAD_REQUEST)

        try:
            order = orders_models.OrderModel.objects.get(
                id=order_id
            )
        except orders_models.OrderModel.DoesNotExist:
            return Response({
                "status": f"Не был найден заказ с {order_id=}."
            }, status.HTTP_400_BAD_REQUEST)

        try:
            payment = models.PaymentModel.get(
                order_id=order_id
            )
        except models.PaymentModel.DoesNotExist:
            payment_description = order.product.name

            payment = models.PaymentModel.create(
                amount=order.amount,
                order_id=order.pk,
                description=payment_description
            )

            receipt = payment.with_receipt()

            items = payment.with_items([
                {
                    "product": order.product,
                    "price": order.product.price,
                    "quantity": 1,
                    "amount": order.amount,
                }
            ])

            merchant_api.init(payment)

            payment.save()

        serializer = self.serializer_class(
            payment
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


@extend_schema_view(
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
class QrPaymentView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [StaticHTMLRenderer]

    def get(self, request: Request):
        payment_id = request.query_params.get("payment_id")
        
        if not payment_id:
            return Response({
                "status": "Не передан payment_id."
            }, status.HTTP_400_BAD_REQUEST)

        try:
            payment = models.PaymentModel.objects.get(
                pk=payment_id
            )
        except models.PaymentModel.DoesNotExist:
            return Response({
                "status": f"Не была найдена оплата с {payment_id=}."
            }, status.HTTP_400_BAD_REQUEST)

        qr = merchant_api.get_qr(payment)

        return Response(
            qr,
            status.HTTP_200_OK
        )


@extend_schema_view(
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
class CancelPaymentView(APIView):
    serializer_class = serializers.PaymentSerializer
    permission_classes = [AllowAny]

    def get(self, request: Request):
        payment_id = request.query_params.get("payment_id")
        
        if not payment_id:
            return Response({
                "status": "Не передан payment_id."
            }, status.HTTP_400_BAD_REQUEST)

        try:
            payment = models.PaymentModel.objects.get(
                pk=payment_id
            )
        except models.PaymentModel.DoesNotExist:
            return Response({
                "status": f"Не была найдена оплата с {payment_id=}."
            }, status.HTTP_400_BAD_REQUEST)

        payment = merchant_api.cancel(payment)
        payment.save()

        serializer = self.serializer_class(payment)

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


@extend_schema_view(
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
class SbpPayTestView(APIView):
    serializer_class = serializers.PaymentSerializer
    permission_classes = [AllowAny]

    def get(self, request: Request):
        payment_id = request.query_params.get("payment_id")
        is_expired = bool(request.query_params.get("is_expired", False))
        is_rejected = bool(request.query_params.get("is_rejected", False))
        
        if not payment_id:
            return Response({
                "status": "Не передан payment_id."
            }, status.HTTP_400_BAD_REQUEST)

        try:
            payment = models.PaymentModel.objects.get(
                pk=payment_id
            )
        except models.PaymentModel.DoesNotExist:
            return Response({
                "status": f"Не была найдена оплата с {payment_id=}."
            }, status.HTTP_400_BAD_REQUEST)

        payment = merchant_api.spb_pay_test(
            payment, is_expired, is_rejected
        )
        payment.save()

        serializer = self.serializer_class(payment)

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
