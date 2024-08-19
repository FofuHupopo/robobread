from django.urls import path

from . import views


urlpatterns = [
    path("", views.AnalyticsView.as_view(), name="index"),
    path("product_stock", views.ProductStockView.as_view(), name="product_stock"),
    path("vending_machines", views.VendingMachinesView.as_view(), name="vending_machines"),
]
