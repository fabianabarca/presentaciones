from django.urls import re_path

from .consumers import DeckSliderConsumer

websocket_urlpatterns = [
    re_path(r"^ws/deck/slider/(?P<deck_id>\w+)/$", DeckSliderConsumer.as_asgi()),
]