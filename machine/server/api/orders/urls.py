from django.urls import path

from . import views


urlpatterns = [
    path("order", views.OrderListView.as_view(), name="orders__order_list"),
    path("order/<str:pk>", views.OrderDetailView.as_view(), name="orders__order_detail"),
]
