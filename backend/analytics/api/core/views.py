from rest_framework import permissions
from rest_framework import generics

from . import serializers
from . import models
from . import docs


@docs.vending_machines_list
class VendingMachinesListView(generics.ListCreateAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)


@docs.vending_machine_detail
class VendingMachineDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
