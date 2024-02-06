from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Room, Message, Shared_file
# from app.models import Profile

class ChatConsumers(AsyncWebsocketConsumer):
    # connected_channels = set()
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = "chat_%s" % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        # self.connected_channels.add(self.channel_name)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        print(data)

        
        if data['type'] == 'chat_message':
            message = data['message']
            username = data['username']
            room = data['room']

            await self.save_message(username, room, message)
            
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'room': room
                }
            )
        
        if  data['type'] == 'file_manage':
            file = data['fileURL']
            uname = data['username']
            rname = data['room']

            await self.save_file(file, uname, rname)

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'file_manage',
                    'fileURL': file,
                    'username': uname,
                    'room': rname
                }
            )

    async def chat_message(self, event):
        print('event Message', event)
        message = event['message']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'room': room
        }))

    @sync_to_async
    def save_message(self, username, room, message):
        user  = User.objects.get(username=username)
        room = Room.objects.get(slug=room)


        Message.objects.create(user=user, room=room, content=message)


    async def file_manage(self, event):
        print('Event image', event)
        file = event['fileURL']
        uname = event['username']
        rname = event['room']

        await self.send(text_data=json.dumps({
            'type': 'file_manage',
            'fileURL': file,
            'username': uname,
            'room': rname
        }))


    @sync_to_async
    def save_file(self, file, uname, rname):
        uploader = User.objects.get(username=uname)
        roomname = Room.objects.get(slug=rname)
        Shared_file.objects.create(uploader=uploader, file=file, room=roomname)