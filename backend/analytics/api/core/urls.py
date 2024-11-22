from django.urls import path

from . import views


urlpatterns = [
    path("vending-machine", views.VendingMachinesListView.as_view(), name="vending_machines"),
    path("vending-machine/<int:pk>", views.VendingMachineDetailView.as_view(), name="vending_machines"),
]
