from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework import generics

from . import serializers
from . import models
from . import services


class VendingMachinesListView(generics.ListCreateAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = super().get_queryset()

        for vending_machine in queryset:
            services.VendingMachineService(vending_machine).sync()
        
        return super().get_queryset()


class VendingMachineDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
