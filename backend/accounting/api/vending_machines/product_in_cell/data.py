from typing import List

from dataclasses import dataclass, field

from api.vending_machines.vending_machines.data import VendingMachineData
from api.products.models import ProductModel


@dataclass
class ProductInCellData:
    id: int = -1
    upload_date: str = ""
    expiration_date: str = ""


@dataclass
class CellData:
    id: int = -1
    products: List[ProductInCellData] = field(default_factory=list)
    number: int = -1
    count: int = -1
    max_count: int = -1
    product: ProductModel = None


@dataclass
class ProductsInCellData(VendingMachineData):
    cells: List[CellData] = field(default_factory=list)
