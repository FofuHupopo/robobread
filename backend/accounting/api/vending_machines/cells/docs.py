from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiTypes
from rest_framework import status

from .serializers import CellDataSerializer, CreateCellDataSerializer, UpdateCellDataSerializer


vending_machine_cell_list = extend_schema_view(
    get=extend_schema(
        summary="Получение списка ячеек в автомате",
        description="Получение списка ячеек в автомате",
        responses={
            status.HTTP_200_OK: CellDataSerializer
        },
        tags=["Ячейки автомата"],
    ),
    post=extend_schema(
        summary="Добавление ячейки в автомат",
        description="Добавление ячейки в автомат",
        request=CreateCellDataSerializer,
        responses={
            status.HTTP_201_CREATED: CellDataSerializer
        },
        tags=["Ячейки автомата"],
    ),
    delete=extend_schema(
        summary="Удаление ячейки из автомата",
        description="Удаление ячейки из автомата",
        parameters=[
            OpenApiParameter(
                name='cell_id',
                location=OpenApiParameter.QUERY,
                description='ID ячейки',
                type=OpenApiTypes.INT,
                required=True
            )
        ],
        responses={
            status.HTTP_200_OK: CellDataSerializer,
            status.HTTP_403_FORBIDDEN: {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Нельзя удалить непустую ячейку с товароми"
                    }
                }
            },
        },
        tags=["Ячейки автомата"],
    ),
    put=extend_schema(
        summary="Обновление ячейки в автомате",
        description="Обновление ячейки в автомате",
        request=UpdateCellDataSerializer,
        responses={
            status.HTTP_200_OK: CellDataSerializer
        },
        tags=["Ячейки автомата"],
    )
)
