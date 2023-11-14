from django.urls import re_path
# from django.urls import path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer)
    # path('chat_doctor/<str:room_name>/',consumers.ChatRoomConsumer.as_asgi())
    # re_path(r'ws//chat_doctor/(?P<room_name>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
    # re_path(r'^ws/(?P<room_name>[^/]+)/$', consumers.ChatRoomConsumer.as_asgi()),
    
]   