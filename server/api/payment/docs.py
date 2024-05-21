from rest_framework import serializers


class OrderIdBodyParamater(serializers.Serializer):
    order_id = serializers.UUIDField()
    

class PaymentIdBodyParamater(serializers.Serializer):
    payment_id = serializers.UUIDField()
