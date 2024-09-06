from typing import List

from dataclasses import dataclass, field

from api.vending_machines.data import VendingMachineData
from . import models


@dataclass
class CategoryData(VendingMachineData):
    categories: List[models.CategoryModel] = field(default_factory=list)


@dataclass
class ProductData(VendingMachineData):
    products: List[models.ProductModel] = field(default_factory=list)
