from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ..models import VendingMachineModel
from api.products.models import CategoryModel
from . import services
from . import serializers
from .utils import get_category_by_sku
from api.vending_machines.vending_machines.utils import get_vending_machine


class VendingMachineCategoryListView(APIView):
    serializer_class = serializers.CategoryDataSerializer
    service_class = services.CategoryService

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
        
        category_sku = request.data.get("category_sku")
        category = get_category_by_sku(category_sku)

        service = self.service_class(vending_machine)
        service.create_category(category)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
    
    def delete(self, request: Request, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)
        
        category_sku = request.data.get("category_sku")
        category = get_category_by_sku(category_sku)
        
        service = self.service_class(vending_machine)
        service.delete_category(category)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def put(self, request: Request, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)
        
        category_sku = request.data.get("category_sku")
        category = get_category_by_sku(category_sku)
        
        service = self.service_class(vending_machine)
        service.update_category(category)

        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
