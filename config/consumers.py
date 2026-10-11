import json

from asgiref.sync import async_to_sync   # used for channel layer
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer




class ChatConsumer(WebsocketConsumer):
    
    #this functon make model for message from client to selver 
    def new_message(self,data):
        print("yes")
    #show perivious message
    def feach_message(self):
        pass
    
    
    
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
    
    # save some function address
    commands={
        
        "new_messge":new_message,
        "feach_message":feach_message,
        
    }

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # give data from command and what to do 
        command = text_data_json["command"]
        
        
        # make function for command
        self.commands[command](self,message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))




# class ChatConsumer(AsyncWebsocketConsumer):
    # async def connect(self):
    #     self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
    #     self.room_group_name = f"chat_{self.room_name}"

    #     # Join room group
    #     await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    #     await self.accept()

    # async def disconnect(self, close_code):
    #     # Leave room group
    #     await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # # Receive message from WebSocket
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]

    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name, {"type": "chat_message", "message": message}
    #     )

    # # Receive message from room group
    # async def chat_message(self, event):
    #     message = event["message"]

    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({"message": message}))







