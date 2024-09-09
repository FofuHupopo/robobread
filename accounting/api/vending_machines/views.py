from rest_framework import generics
from rest_framework import permissions

from . import serializers
from . import models
from . import docs


@docs.vending_machine_list
class VendingMachineListView(generics.ListCreateAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)


@docs.vending_machine_detail
class VendingMachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)
