from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import ProductService
from .serializers import ProductDataSerializer
from .utils import get_product_by_sku
from api.vending_machines.vending_machines.utils import get_vending_machine


class VendingMachineProductListView(APIView):
    serializer_class = ProductDataSerializer
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
    
    def _product_by_sku(self, product_sku: str):
        product = get_product_by_sku(product_sku)

        return product

    def get(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        return self._sync(service)

    def post(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        product = self._product_by_sku(request.data.get("product_sku"))

        service.create_product(product)

        return self._sync(service)
    
    def delete(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        product = self._product_by_sku(request.data.get("product_sku"))

        service.delete_product(product)

        return self._sync(service)

    def put(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        product = self._product_by_sku(request.data.get("product_sku"))

        service.update_product(product)

        return self._sync(service)
