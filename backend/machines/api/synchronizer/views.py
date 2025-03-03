from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models
from api.permissions import MachinePermission


class RegisterMachineView(APIView):
    serializer_class = serializers.RegisterMachineSerializer

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            if serializer.errors.get('sku') and serializer.errors['sku'][0].code == 'unique':
                try:
                    machine = models.MachineModel.objects.get(
                        sku=serializer.initial_data['sku']
                    )
                    
                    serializer = serializers.MachineSerializer(machine)

                    return Response(
                        serializer.data,
                        status.HTTP_200_OK
                    )
                except models.MachineModel.DoesNotExist:
                    pass

            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        machine = serializer.create(serializer.validated_data)
        serializer = serializers.MachineSerializer(machine)

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )


class BaseMachineView(APIView):
    permission_classes = [MachinePermission]
    model = None
    serializer_class = None

    def post(self, request: Request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        serializer.save(machine=request.machine)

        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )

    def get(self, request: Request):
        objects = self.model.objects.filter(machine_id=request.machine.id)
        serializer = self.serializer_class(objects, many=True)

        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
    
    def delete(self, request: Request, key: str):
        try:
            filter_params = {
                self.model.key(): key,
                'machine_id': request.machine.id
            }
            obj = self.model.objects.get(**filter_params)
            obj.delete()
        except self.model.DoesNotExist:
            return Response(
                {"message": f"{self.model.__name__} not found"},
                status.HTTP_404_NOT_FOUND
            )

        return Response(
            status.HTTP_204_NO_CONTENT
        )

    def put(self, request: Request, key: str):
        try:
            filter_params = {
                self.model.key(): key,
                'machine_id': request.machine.id
            }
            obj = self.model.objects.get(**filter_params)
        except self.model.DoesNotExist:
            return Response(
                {"message": f"{self.model.__name__} not found"},
                status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(obj, data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


class MachineOrderView(BaseMachineView):
    model = models.MachineOrderModel
    serializer_class = serializers.MachineOrderSerializer

class MachineCategoryView(BaseMachineView):
    model = models.MachineCategoryModel
    serializer_class = serializers.MachineCategorySerializer


class MachineProductView(BaseMachineView):
    model = models.MachineProductModel
    serializer_class = serializers.MachineProductSerializer


class MachineCellView(BaseMachineView):
    model = models.MachineCellModel
    serializer_class = serializers.MachineCellSerializer


class MachineProductInCellView(BaseMachineView):
    model = models.MachineProductInCellModel
    serializer_class = serializers.MachineProductInCellSerializer
