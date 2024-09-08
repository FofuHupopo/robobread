from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from . import services
from .utils import get_vending_machine


@extend_schema_view(
    get=extend_schema(
        summary="Синхронизация данных для одного аппарата",
        description="Синхронизация данных для одного аппарата",
        responses={200: serializers.VendingMachineDataSerializer},
    )
)
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


@extend_schema_view(
    get=extend_schema(
        summary="Синхронизация данных для всех аппаратов",
        description="Синхронизация данных для всех аппаратов",
        responses={200: serializers.VendingMachineDataSerializer(many=True)},
    )
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

