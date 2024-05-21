from django.urls import path

from . import views


urlpatterns = [
    path("payment", views.PaymentView.as_view(), name="payment__payment"),
    path("payment/cancel", views.CancelPaymentView.as_view(), name="payment__payment_cancel"),
]
