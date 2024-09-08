from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .services import CategoryService
from .serializers import CategoryDataSerializer
from .utils import get_category_by_sku
from api.vending_machines.vending_machines.utils import get_vending_machine


class VendingMachineCategoryListView(APIView):
    serializer_class = CategoryDataSerializer
    service_class = CategoryService

    def _sync(self, service: CategoryService):
        serializer = self.serializer_class(
            service.sync()
        )

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    def _service(self, vending_machine_id: int):
        vending_machine = get_vending_machine(vending_machine_id)

        service = self.service_class(vending_machine)

        return service

    def _category_by_sku(self, category_sku: str):
        category = get_category_by_sku(category_sku)

        return category

    def get(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        return self._sync(service)

    def post(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        category = self._category_by_sku(request.data.get("category_sku"))

        service.create_category(category)

        return self._sync(service)

    def delete(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        category = self._category_by_sku(request.data.get("category_sku"))

        service.delete_category(category)

        return self._sync(service)

    def put(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        category = self._category_by_sku(request.data.get("category_sku"))

        service.update_category(category)

        return self._sync(service)
