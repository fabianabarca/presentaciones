import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from decks.models import Answer, Session


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

        if "answer" in text_data_json:
            await self.save_answer(text_data_json)

        else:
            indexh = text_data_json["indexh"]
            indexv = text_data_json["indexv"]

            # Send message to demo group
            await self.channel_layer.group_send(
                self.deck_group_name,
                {
                    "type": "slide_changed",
                    "message": {"indexh": indexh, "indexv": indexv},
                },
            )

    # Receive message from room group
    async def slide_changed(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @sync_to_async
    def save_answer(self, answer_data):
        print(answer_data)
        answer_text = answer_data["answer"]
        session_id = answer_data["session_id"]
        question_id = answer_data["question_id"]
        user_id = answer_data["user_id"]

        session = Session.objects.get(session_id=int(session_id))
        answer = Answer.objects.create(
            question_id=int(question_id),
            user_id=user_id,
            answer_text=answer_text,
            session_id=session,
        )

        answer.save()
