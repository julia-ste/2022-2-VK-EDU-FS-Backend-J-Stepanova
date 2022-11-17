from django.urls import path

from chats.views.chat_views import ChatRetrieveUpdateDestroy, ChatCreate, ChatList, ChatMemberCreate
from chats.views.message_views import MessageList, MessageCreate, MessageRetrieveUpdateDestroy, MessageRead

urlpatterns = [
    path("<int:user_pk>/", ChatList.as_view(), name="chat_list"),
    path("new/", ChatCreate.as_view(), name="chat_create"),
    path("detail/<int:pk>/", ChatRetrieveUpdateDestroy.as_view(), name="chat_detail"),
    path("<int:chat_pk>/add-member/", ChatMemberCreate.as_view(), name="chat_member_create"),

    path("<int:chat_pk>/messages/", MessageList.as_view(), name="message_list"),
    path("<int:chat_pk>/messages/new/", MessageCreate.as_view(), name="message_create"),
    path("messages/<int:pk>", MessageRetrieveUpdateDestroy.as_view(), name="message_detail"),
    path("messages/read/<int:pk>", MessageRead.as_view(), name="message_read"),
]
