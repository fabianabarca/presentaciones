from django.urls import re_path

from .consumers import DeckConsumer

websocket_urlpatterns = [
    re_path(r"ws/decks/(?P<deck_id>\w+)/$", DeckConsumer.as_asgi()),
]