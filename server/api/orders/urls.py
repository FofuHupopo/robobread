from django.urls import path

from . import views


urlpatterns = [
    path("order", views.OrderListAPIView.as_view(), name="orders__order_list"),
    path("order/<str:pk>", views.OrderDetailAPIView.as_view(), name="orders__order_detail"),
]
