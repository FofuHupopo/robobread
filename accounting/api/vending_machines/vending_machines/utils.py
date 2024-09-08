from api.exceptions import NoObjectException
from ..models import VendingMachineModel


def get_vending_machine(vending_machine_id: int) -> VendingMachineModel:
    try:
        vending_machine = VendingMachineModel.objects.get(
            pk=vending_machine_id
        )
    except VendingMachineModel.DoesNotExist:
        raise NoObjectException(
            "Vending machine not found",
            {"message": f"Vending machine with id=\"{vending_machine_id}\" not found"},
        )

    return vending_machine
