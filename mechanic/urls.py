from django.urls import path
from .views import index, pending_order

urlpatterns = [
    path('', index),
    path('pending_order/', pending_order)
]
