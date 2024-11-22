from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("statistics/", include("api.statistics.urls")),
    path("vending-machines/", include("api.core.urls")),
]

if hasattr(settings, "DEBUG") and getattr(settings, "DEBUG"):
    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    ]
