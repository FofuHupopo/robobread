from typing import List
from dataclasses import dataclass

from api.core.services import VendingMachineData
from .. import models


@dataclass
class ProductData(VendingMachineData):
    product_stock: List[models.ProductStockModel] = None
