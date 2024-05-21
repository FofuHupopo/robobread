import os
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from api.orders import models as orders_models
from .services import MerchantAPI
from . import models
from . import docs
from . import serializers


merchant_api = MerchantAPI(
    terminal_key=os.getenv("TERMINAL_KEY"),
    secret_key=os.getenv("SECRET_KEY"),
)


class PaymentView(APIView):
    serializer_class = serializers.PaymentSerializer
    permission_classes = [AllowAny]
    
    @extend_schema(
        parameters=[
            OpenApiParameter("payment_id", OpenApiTypes.STR)
        ]
    )
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

        merchant_api.status(payment)
        payment.save()

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

    @extend_schema(
        request=docs.OrderIdBodyParamater
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
        
        
class QrPaymentView(APIView):
    serializer_class = serializers.PaymentSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="payment_id",
                type=OpenApiTypes.STR
            )
        ]
    )
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

        payment = merchant_api.get_qr(payment)
        payment.save()

        serializer = self.serializer_class(payment)

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


class CancelPaymentView(APIView):
    serializer_class = serializers.PaymentSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="payment_id",
                type=OpenApiTypes.STR
            )
        ]
    )
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
