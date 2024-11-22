
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import ProductsInCellService
from .serializers import ProductsInCellSerializer
from api.vending_machines.vending_machines.utils import get_vending_machine

from . import docs


@docs.vending_machine_products_in_cell_list
class VendingMachineProductsInCellListView(APIView):
    serializer_class = ProductsInCellSerializer
    service_class = ProductsInCellService

    def _sync(self, service: ProductsInCellService, status_=status.HTTP_200_OK):
        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status_
        )
    
    def _service(self, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)

        service = self.service_class(vending_machine)

        return service

    def get(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        return self._sync(service, status.HTTP_200_OK)

    def put(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        serializer = self.serializer_class(
            data=request.data
        )

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        service.update_cells(serializer.data)

        return self._sync(service, status.HTTP_200_OK)
