from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiTypes
from rest_framework import status


check_code = extend_schema_view(
    get=extend_schema(
        summary="Проверка кода для открытия двери",
        description="Проверка кода для открытия двери",
        parameters=[
            OpenApiParameter(
                name="code",
                location=OpenApiParameter.QUERY,
                type=OpenApiTypes.STR,
                required=True,
            )
        ],
        responses={
            status.HTTP_200_OK: {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "ok"
                    }
                }
            },
            status.HTTP_400_BAD_REQUEST: {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "No code in query params"
                    }
                }
            },
            status.HTTP_403_FORBIDDEN: {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Code is incorrect"
                    }
                }
            },

        },
        tags=["Безопасность"],
    )
)

vending_machine_info = extend_schema_view(
    get=extend_schema(
        summary="Получение информации об автомате",
        description="Получение статической локальной информации об автомате",
        responses={
            status.HTTP_200_OK: {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "example": "Автомат в ТЦ на первом этаже",
                    },
                    "address": {
                        "type": "string",
                        "example": "Улица Пушкина, дом Колотушкина",
                    }
                }
            }
        },
        tags=["Безопасность"],
    )
)
