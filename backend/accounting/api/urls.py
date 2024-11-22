from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("vending-machines/", include(
        "api.vending_machines.urls",
        namespace="vending_machines"
    )),
    path("products/", include(
        "api.products.urls",
        namespace="products"
    )),
    path("packing/", include(
        "api.packing.urls",
        namespace="packing"
    )),
]

if hasattr(settings, "DEBUG") and getattr(settings, "DEBUG"):
    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    ]
