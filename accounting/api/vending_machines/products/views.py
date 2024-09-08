from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import services
from . import serializers
from .utils import get_product_by_sku
from api.vending_machines.vending_machines.utils import get_vending_machine


class VendingMachineProductListView(APIView):
    serializer_class = serializers.ProductDataSerializer
    service_class = services.ProductService

    def get(self, request: Request, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)

        serializer = self.serializer_class(
            self.service_class(vending_machine).sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def post(self, request: Request, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)
        
        product_sku = request.data.get("product_sku")
        product = get_product_by_sku(product_sku)

        service = self.service_class(vending_machine)
        service.create_product(product)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
    
    def delete(self, request: Request, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)
        
        product_sku = request.data.get("product_sku")
        product = get_product_by_sku(product_sku)

        service = self.service_class(vending_machine)
        service.delete_product(product)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def put(self, request: Request, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)
        
        product_sku = request.data.get("product_sku")
        product = get_product_by_sku(product_sku)
        
        service = self.service_class(vending_machine)
        service.update_product(product)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
