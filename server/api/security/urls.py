from django.urls import path

from . import views


urlpatterns = [
    path("check-code", views.CheckCodeView.as_view(), name="security__check_code"),
]
