from typing import List, Mapping
from django.utils.timezone import datetime, timedelta

from .data import SaleData


class SalesStatistics:
    def __init__(self, data_objects: List[SaleData]) -> None:
        self.data_objects = data_objects

    def by_category(self) -> Mapping[str, int]:
        sales_by_category = {}
        total_sales = 0

        for data_object in self.data_objects:
            for sale in data_object.sales:
                if not sale.is_paid:
                    continue

                if sale.category_name not in sales_by_category:
                    sales_by_category[sale.category_name] = 0
                
                sales_by_category[sale.category_name] += 1
                total_sales += 1
        
        return {
            "category": sales_by_category,
            "total": total_sales,
        }

    def by_product(self) -> Mapping[str, int]:
        sales_by_product = {}
        total_sales = 0

        for data_object in self.data_objects:
            for sale in data_object.sales:
                if not sale.is_paid:
                    continue

                if sale.product_name not in sales_by_product:
                    sales_by_product[sale.product_name] = 0
                
                sales_by_product[sale.product_name] += 1
                total_sales += 1
        
        return {
            "product": sales_by_product,
            "total": total_sales,
        }

    def percent_of_redemption(self) -> Mapping[str, float]:
        redemption = 0
        total = 0

        for data_object in self.data_objects:
            for sale in data_object.sales:
                if sale.is_paid:
                    redemption += 1
                
                total += 1
        
        return {
            "percent": f"{redemption / total * 100:.2f}"
        }

    def revenue(self) -> Mapping[str, float]:
        revenue = 0

        for data_object in self.data_objects:
            for sale in data_object.sales:
                if not sale.is_paid:
                    continue

                revenue += sale.amount
        
        print(revenue)

        return {
            "revenue": revenue
        }

    def revenue_for_the_week(self) -> Mapping[str, float]:
        revenue_for_the_week = [0] * 7
        date_list = []
        total = 0

        current_date = datetime.now()
        one_week_ago = current_date - timedelta(days=7)

        for data_object in self.data_objects:
            for sale in data_object.sales:
                if not sale.is_paid:
                    continue

                if sale.created_at.date() < one_week_ago.date():
                    continue

                print(sale.created_at)

                current_day = sale.created_at.date().day
                index = current_day - one_week_ago.date().day

                revenue_for_the_week[index] += sale.amount
                total += sale.amount

        print(revenue_for_the_week)

        
        return {
            "revenue_for_the_week": revenue_for_the_week,
            "total": total
        }
