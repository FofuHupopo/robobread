from django.urls import path

from . import views


app_name = 'vending_machines'

urlpatterns = [
    path("vending-machine", views.VendingMachineListView.as_view(), name="vending_machine_list"),
    path("vending-machine/<int:pk>", views.VendingMachineDetailView.as_view(), name="vending_machine_detail"),
    
    path("sync", views.SyncVendingMachinesView.as_view(), name="vending_machine_sync")
]
