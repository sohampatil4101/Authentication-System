from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'tester_message',
                'tester': 'hello world',
            }
        )

    async def tester_mesage(self, event):
        tester = event['tester']
        await self.send(text_data= json.dumps({
            'tester': tester,
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.load(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group,
            {
                'type': 'chatroom_message',
                'message': message,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']

        await self.send(text_data = json.dumps({
            'message': message,
        }))

    pass

