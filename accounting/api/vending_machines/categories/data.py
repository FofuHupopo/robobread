from typing import List

from dataclasses import dataclass, field

from api.vending_machines.vending_machines.data import VendingMachineData
from api.products.models import CategoryModel


@dataclass
class CategoryData(VendingMachineData):
    categories: List[CategoryModel] = field(default_factory=list)
