from typing import List

from api.core.services import VendingMachineService
from .. import models
from .data import SaleData


URLS = {
    "sales": "orders/order",
}


class SaleService(VendingMachineService):
    def __init__(self, vending_machine: models.VendingMachineModel) -> None:
        super().__init__(vending_machine)

        self.update_urls(URLS)
    
    def active_sync(self) -> SaleData:
        data_object = SaleData()

        data_object.sales = self._sync_sales()

        return data_object

    def inactive_sync(self) -> SaleData:
        return SaleData(
            sales=models.SalesModel.objects.filter(
                vending_machine=self.vending_machine
            ),
        )

    def _sync_sales(self) -> List[models.SalesModel]:
        response = self._request(self.URLS["sales"])

        sales = []

        for order in response:
            sales.append(
                models.SalesModel.objects.get_or_create(
                    vending_machine=self.vending_machine,
                    order_id=order["id"],
                    amount=order["amount"],
                    created_at=order["created_at"],
                    product_id=order["product"]["id"],
                    product_name=order["product"]["name"],
                    category_id=order["product"]["category"]["id"],
                    category_name=order["product"]["category"]["name"],
                    is_paid=order["is_paid"]
                )[0]
            )

        return sales
