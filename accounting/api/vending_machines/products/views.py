from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import ProductService
from .serializers import ProductDataSerializer
from .utils import get_product_by_sku
from .docs import ProductRequestSerializer
from api.vending_machines.vending_machines.utils import get_vending_machine


@extend_schema_view(
    get=extend_schema(
        summary="Получение списка продуктов в автомате",
        description="Получение списка продуктов в автомате",
        responses={
            status.HTTP_200_OK: ProductDataSerializer
        }
    ),
    post=extend_schema(
        summary="Добавление продукта в список автомата",
        description="Добавление продукта в список автомата",
        request=ProductRequestSerializer,
        responses={
            status.HTTP_201_CREATED: ProductDataSerializer
        }
    ),
    delete=extend_schema(
        summary="Удаление продукта из списка автомата",
        description="Удаление продукта из списка автомата",
        parameters=[
            OpenApiParameter(
                name='product_sku',
                location=OpenApiParameter.QUERY,
                description='ID продукта',
                type=OpenApiTypes.INT,
                required=True
            )
        ],
        responses={
            status.HTTP_200_OK: ProductDataSerializer
        }
    ),
    put=extend_schema(
        summary="Обновление продукта в списке автомата",
        description="Обновление продукта в списке автомата",
        request=ProductRequestSerializer,
        responses={
            status.HTTP_200_OK: ProductDataSerializer
        }
    )
)
class VendingMachineProductListView(APIView):
    serializer_class = ProductDataSerializer
    service_class = ProductService

    def _sync(self, service: ProductService, status_=status.HTTP_200_OK):
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
    
    def _product_by_sku(self, product_sku: str):
        product = get_product_by_sku(product_sku)

        return product

    def get(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        return self._sync(service, status.HTTP_200_OK)

    def post(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        product = self._product_by_sku(request.data.get("product_sku"))

        service.create_product(product)

        return self._sync(service, status.HTTP_201_CREATED)
    
    def delete(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        product = self._product_by_sku(request.query_params.get("product_sku"))

        service.delete_product(product)

        return self._sync(service, status.HTTP_200_OK)

    def put(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        product = self._product_by_sku(request.data.get("product_sku"))

        service.update_product(product)

        return self._sync(service, status.HTTP_200_OK)
