from typing import List

from dataclasses import dataclass, field

from api.vending_machines.vending_machines.data import VendingMachineData
from api.products.models import ProductModel


@dataclass
class ProductData(VendingMachineData):
    products: List[ProductModel] = field(default_factory=list)
