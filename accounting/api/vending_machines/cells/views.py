from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import ProductService
from .data import UpdateCellData, CreateCellData
from .serializers import CellDataSerializer, CreateCellDataSerializer, UpdateCellDataSerializer
from api.vending_machines.vending_machines.utils import get_vending_machine


class VendingMachineCellListView(APIView):
    serializer_class = CellDataSerializer
    service_class = ProductService

    def _sync(self, service: ProductService):
        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
    
    def _service(self, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)

        service = self.service_class(vending_machine)

        return service

    def get(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        return self._sync(service)

    def post(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        
        cell = CreateCellDataSerializer(data=request.data)

        if not cell.is_valid():
            return Response(
                cell.errors,
                status.HTTP_400_BAD_REQUEST
            )
        
        cell_data: CreateCellData = cell.validated_data

        service.create_cell(cell_data)

        return self._sync(service)
    
    def delete(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        cell_id = request.data.get("cell_id")

        service.delete_cell(cell_id)

        return self._sync(service)

    def put(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        cell = UpdateCellDataSerializer(data=request.data)

        if not cell.is_valid():
            return Response(
                cell.errors,
                status.HTTP_400_BAD_REQUEST
            )
        
        cell_data: UpdateCellData = cell.validated_data

        service.update_cell(cell_data.id, cell_data)

        return self._sync(service)
