# app/routing.py

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/davyd/', consumers.MyConsumer.as_asgi()),
]
