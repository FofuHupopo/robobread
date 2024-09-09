from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from . import services
from .utils import get_vending_machine
from . import docs


@docs.sync_one_vending_machine
class SyncOneVendingMachineView(APIView):
    serializer_class = serializers.VendingMachineDataSerializer

    def get(self, request: Request, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)

        serializer = self.serializer_class(
            services.VendingMachineService(
                vending_machine
            ).sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


@docs.sync_vending_machines
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

