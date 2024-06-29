from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from constance import config

from api.utils import InteractionCommand


class CheckCodeView(APIView):
    def get(self, request: Request):
        code = request.query_params.get("code")
        
        if not code:
            return Response({
                "message": "not code in query params"
            }, status.HTTP_400_BAD_REQUEST)
        
        if code == config.LOCK_CODE:
            InteractionCommand.open_door()

            return Response({
                "message": "ok"
            }, status.HTTP_200_OK)
        else:
            return Response({
                "message": "Code is not correct"
            }, status.HTTP_400_BAD_REQUEST)
