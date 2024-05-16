import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DeckSliderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.deck_id = self.scope["url_route"]["kwargs"]["deck_id"]
        self.deck_group_name = f"deck_{self.deck_id}"
        print(self.deck_group_name)
        print(self.channel_name)
        print(self.deck_id)

        # Join demo group
        await self.channel_layer.group_add(self.deck_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.deck_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        indexh = text_data_json["indexh"]
        indexv = text_data_json["indexv"]

        # Send message to demo group
        await self.channel_layer.group_send(
            self.deck_group_name,
            {"type": "slide_changed", "message": {"indexh": indexh, "indexv": indexv}},
        )

    # Receive message from room group
    async def slide_changed(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
