from django.urls import path

from . import views


urlpatterns = [
    path("sales/by-category", views.SalesByCategoryView.as_view(), name="statistics__sales_by_category"),
    path("sales/by-product", views.SalesByProductView.as_view(), name="statistics__sales_by_product"),
    path("sales/percent-of-redemption", views.PercentOfRedemptionView.as_view(), name="statistics__sales_percent_of_redemption"),
    path("sales/revenue", views.RevenueView.as_view(), name="statistics__sales_revenue"),
    path("sales/revenue-for-the-week", views.RevenueForTheWeekView.as_view(), name="statistics__sales_revenue_for_the_week"),

    path("product-stock/all", views.AllProductStockView.as_view(), name="statistics__product_stock_all"),
]
