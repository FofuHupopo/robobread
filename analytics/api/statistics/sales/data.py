from typing import List
from dataclasses import dataclass

from api.core.services import VendingMachineData
from .. import models


@dataclass
class SaleData(VendingMachineData):
    sales: List[models.SalesModel] = None
