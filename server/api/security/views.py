import os

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from constance import config
from dotenv import load_dotenv

from api.utils import InteractionCommand


load_dotenv()


@extend_schema_view(
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
class CheckCodeView(APIView):
    def get(self, request: Request):
        code = request.query_params.get("code")
        
        if not code:
            return Response({
                "message": "No code in query params"
            }, status.HTTP_400_BAD_REQUEST)
        
        if code == config.LOCK_CODE:
            InteractionCommand.open_door()

            return Response({
                "message": "ok"
            }, status.HTTP_200_OK)
        else:
            return Response({
                "message": "Code is incorrect"
            }, status.HTTP_403_FORBIDDEN)


@extend_schema_view(
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
class VendingMachineInfoView(APIView):
    def get(self, request: Request):
        return Response({
            "name": os.getenv("VENDING_MACHINE_NAME"),
            "address": os.getenv("VENDING_MACHINE_ADDRESS")
        }, status.HTTP_200_OK)
