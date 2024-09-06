from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions

from . import serializers
from . import models
from . import services


class VendingMachineListView(generics.ListCreateAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)


class VendingMachineDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.VendingMachineSerializer
    queryset = models.VendingMachineModel.objects.all()
    permission_classes = (permissions.AllowAny,)


class SyncVendingMachinesView(APIView):
    serializer_class = serializers.VendingMachineDataSerializer

    def get(self, request: Request):
        serializer = self.serializer_class(
            services.VendingMachineService.get_syncronized_vending_machines(),
            many=True
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
