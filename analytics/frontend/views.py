from django.views.generic import TemplateView


class AnalyticsView(TemplateView):
    template_name = "pages/analytics.html"
    extra_context = {}


class ProductStockView(TemplateView):
    template_name = "pages/product_stock.html"
    extra_context = {}


class VendingMachinesView(TemplateView):
    template_name = "pages/vending_machines.html"
    extra_context = {}
