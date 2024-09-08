from rest_framework_dataclasses.serializers import DataclassSerializer

from api.vending_machines.serializers import VendingMachineSerializer
from . import data


class VendingMachineDataSerializer(DataclassSerializer):
    vending_machine = VendingMachineSerializer()

    class Meta:
        dataclass = data.VendingMachineData
        depth = 1
