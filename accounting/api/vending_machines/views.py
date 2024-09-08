from rest_framework import generics
from rest_framework import permissions

from . import serializers
from . import models


class VendingMachineListView(generics.ListCreateAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)


class VendingMachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)
