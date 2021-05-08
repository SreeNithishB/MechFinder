from django.urls import path
from .consumers import WSConsumer


### IMPORTANT NOTE ###

### DO NOT INCLUDE ANY MORE ROUTING HERE. ADD ROUTING ONLU THROUGH MECHANICS 

ws_urlpatterns = [
    path('ws/customer_help_url/', WSConsumer.as_asgi())
]
