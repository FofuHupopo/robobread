from typing import List

from dataclasses import dataclass, field

from api.vending_machines.vending_machines.data import VendingMachineData


@dataclass
class ProductInCellData:
    id: int = -1
    upload_date: str = ""
    expiration_date: str = ""


@dataclass
class ProductDetailData:
    id: int = -1
    name: str = ""
    description: str = ""
    sku: str = ""
    composition: str = ""
    expiration_date: str = ""
    price: int = -1
    image: str = ""


@dataclass
class CellDetailData:
    id: int = -1
    products: List[ProductInCellData] = field(default_factory=list)
    number: int = -1
    count: int = -1
    max_count: int = -1
    product: ProductDetailData = None


@dataclass
class CellData(VendingMachineData):
    cells: List[CellDetailData] = field(default_factory=list)


@dataclass
class CreateCellData:
    number: int
    product_id: int
    max_count: int


@dataclass
class UpdateCellData:
    id: int
    number: int
    max_count: int
    product_id: int
