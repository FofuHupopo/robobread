from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics

from . import models
from . import serializers


class PackingView(generics.ListCreateAPIView):
    queryset = models.PackingModel.objects.all()
    serializer_class = serializers.PackingSerializer


class PackingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.PackingModel.objects.all()
    serializer_class = serializers.PackingSerializer
