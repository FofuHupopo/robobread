from rest_framework import serializers

from . import models


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentModel
        fields = "__all__"
