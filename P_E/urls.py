# from readline import get_endidx
from django.urls import path
from P_E.views import get_products
from P_E.views import get_events

urlpatterns = [
    path("get_products", get_products, name="products"),
    path("get_events", get_events, name="events")
]
