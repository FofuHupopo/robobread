from typing import Dict, List
from pydantic import BaseModel


class StatisticsSalesByCategory(BaseModel):
    category: Dict[str, int]
    total: int


class StatisticsSalesByProduct(BaseModel):
    product: Dict[str, int]
    total: int


class StatisticsSalesPercentOfRedemption(BaseModel):
    percent: float


class StatisticsSalesRevenue(BaseModel):
    revenue: int


class StatisticsSalesRevenueForTheDay(BaseModel):
    value: int
    day: str


class StatisticsSalesRevenueForTheWeek(BaseModel):
    revenue_for_the_week: list[StatisticsSalesRevenueForTheDay]
    total: int


class ProductStock(BaseModel):
    id: int
    product_id: int
    product_name: str
    quantity: int
    max_quantity: int
    vending_machine: int


class VendingMachine(BaseModel):
    id: int
    address: str
    name: str
    ip_address: str
    last_sync_date: str
    status: str


class StatisticsProductStockAll(BaseModel):
    product_stock: List[ProductStock]
    vending_machine: VendingMachine
