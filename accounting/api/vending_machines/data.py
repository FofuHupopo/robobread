from dataclasses import dataclass

from api.services import BaseData
from . import models


@dataclass
class VendingMachineData(BaseData):
    vending_machine: models.VendingMachineModel = None
    is_active: bool = None
