from django.urls import path

from chats.views.chat_views import (
    ChatCreate,
    ChatList,
    ChatMemberCreate,
    ChatMemberDestroy,
    ChatRetrieveUpdateDestroy,
)
from chats.views.message_views import (
    MessageCreate,
    MessageList,
    MessageRead,
    MessageRetrieveUpdateDestroy,
)

urlpatterns = [
    path("", ChatList.as_view(), name="chat_list"),
    path("new/", ChatCreate.as_view(), name="chat_create"),
    path("<int:chat_pk>/", ChatRetrieveUpdateDestroy.as_view(), name="chat_detail"),

    path("<int:chat_pk>/members/new/", ChatMemberCreate.as_view(), name="chat_member_create"),
    path("<int:chat_pk>/members/<int:user_pk>/", ChatMemberDestroy.as_view(), name="chat_member_delete"),

    path("<int:chat_pk>/messages/", MessageList.as_view(), name="message_list"),
    path("<int:chat_pk>/messages/new/", MessageCreate.as_view(), name="message_create"),
    path("<int:chat_pk>/messages/<int:pk>/", MessageRetrieveUpdateDestroy.as_view(), name="message_detail"),
    path("<int:chat_pk>/messages/<int:pk>/read/", MessageRead.as_view(), name="message_read"),
]
