from django.urls import path
from .consumers import WSConsumer
from .consumers_for_finished import WSConsumer as ws_for_finished
from customer.consumers import WSConsumer as customer_ws

ws_urlpatterns = [
    path('ws/mechanic_dashboard_url/', WSConsumer.as_asgi()),
    path('ws/customer_help_url/', customer_ws.as_asgi()),
    path('ws/customer_helps_finished/', ws_for_finished.as_asgi()),
]
