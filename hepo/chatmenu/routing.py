from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/login/chatmenu/(?P<room>\w+)/$', consumers.ChatRoomConsumer.as_asgi()),
]