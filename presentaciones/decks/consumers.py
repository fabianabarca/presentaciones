import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DeckConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.deck_id = self.scope["url_route"]["kwargs"]["deck_id"]
        self.deck_group_name = f"deck_{self.deck_id}"
        print(f"Group name: {self.deck_group_name}")
        print(f"Channel name: {self.channel_name}")

        # Join room group
        await self.channel_layer.group_add(self.deck_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.deck_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        slide = text_data_json["slide"]
        fragment = text_data_json["fragment"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.deck_group_name, {"type": "chat.message", "message": {"slide": slide, "fragment": fragment}}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        print(f"Message: {message}")

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
