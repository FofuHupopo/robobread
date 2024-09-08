from django.urls import path

from . import views
from .vending_machines import views as vending_machine_views
from .categories import views as category_views
from .products import views as product_views
from .cells import views as cell_views


app_name = 'vending_machines'

urlpatterns = [
    path("vending-machine", views.VendingMachineListView.as_view(), name="vending_machine_list"),
    path("vending-machine/<int:pk>", views.VendingMachineDetailView.as_view(), name="vending_machine_detail"),

    path("sync", vending_machine_views.SyncVendingMachinesView.as_view(), name="vending_machine_sync"),
    path("vending-machine/<int:vending_machine_id>/sync", vending_machine_views.SyncOneVendingMachineView.as_view(), name="vending_machine_one_sync"),

    path('vending-machine/<int:vending_machine_id>/category', category_views.VendingMachineCategoryListView.as_view(), name="vending_machine_category_list"),
    path('vending-machine/<int:vending_machine_id>/product', product_views.VendingMachineProductListView.as_view(), name="vending_machine_product_list"),
    path('vending-machine/<int:vending_machine_id>/cell', cell_views.VendingMachineCellListView.as_view(), name="vending_machine_cell_list"),
]
