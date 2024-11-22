import os

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from constance import config
from dotenv import load_dotenv

from . import docs
from api.utils import InteractionCommand


load_dotenv()


@docs.check_code
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


@docs.vending_machine_info
class VendingMachineInfoView(APIView):
    def get(self, request: Request):
        return Response({
            "name": os.getenv("VENDING_MACHINE_NAME"),
            "address": os.getenv("VENDING_MACHINE_ADDRESS")
        }, status.HTTP_200_OK)
