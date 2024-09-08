from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .services import CategoryService
from .serializers import CategoryDataSerializer
from .utils import get_category_by_sku
from . import docs
from api.vending_machines.vending_machines.utils import get_vending_machine


@extend_schema_view(
    get=extend_schema(
        summary="Получение списка категорий в автомате",
        description="Получение списка категорий в автомате",
        responses={
            status.HTTP_200_OK: CategoryDataSerializer
        },
        tags=["Категории автомата"],
    ),
    post=extend_schema(
        summary="Добавление категории в список автомата",
        description="Добавление категории в список автомата",
        request=docs.CategoryRequestSerializer,
        responses={
            status.HTTP_201_CREATED: CategoryDataSerializer
        },
        tags=["Категории автомата"],
    ),
    delete=extend_schema(
        summary="Удаление категории из списка автомата",
        description="Удаление категории из списка автомата",
        parameters=[
            OpenApiParameter(
                name='category_sku',
                location=OpenApiParameter.QUERY,
                description='ID категории',
                type=OpenApiTypes.INT,
                required=True
            )
        ],
        responses={
            status.HTTP_200_OK: CategoryDataSerializer
        },
        tags=["Категории автомата"],
    ),
    put=extend_schema(
        summary="Обновление категории в списке автомата",
        description="Обновление категории в списке автомата",
        request=docs.CategoryRequestSerializer,
        responses={
            status.HTTP_200_OK: CategoryDataSerializer
        },
        tags=["Категории автомата"],
    )
)
class VendingMachineCategoryListView(APIView):
    serializer_class = CategoryDataSerializer
    service_class = CategoryService

    def _sync(self, service: CategoryService, status_: status=status.HTTP_200_OK):
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

    def _category_by_sku(self, category_sku: str):
        category = get_category_by_sku(category_sku)

        return category

    def get(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)

        return self._sync(service, status.HTTP_200_OK)

    def post(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        category = self._category_by_sku(request.data.get("category_sku"))

        service.create_category(category)

        return self._sync(service, status.HTTP_201_CREATED)

    def delete(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        category = self._category_by_sku(request.query_params.get("category_sku"))

        service.delete_category(category)

        return self._sync(service, status.HTTP_200_OK)

    def put(self, request: Request, vending_machine_id: int):
        service = self._service(vending_machine_id)
        category = self._category_by_sku(request.data.get("category_sku"))

        service.update_category(category)

        return self._sync(service, status.HTTP_200_OK)
