from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .. import models
from . import services


class SyncOneVendingMachineView(APIView):
    serializer_class = serializers.VendingMachineDataSerializer

    def get(self, request: Request, vending_machine_id: int):
        try:
            vending_machine = models.VendingMachineModel.objects.get(pk=vending_machine_id)
        except models.VendingMachineModel.DoesNotExist:
            return Response(
                {"message": "Vending machine not found"},
                status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(
            services.VendingMachineService(
                vending_machine
            ).sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


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
