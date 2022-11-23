from django.shortcuts import get_object_or_404

from chats.models import Chat
from chats.serializers import (
    MessageListSerializer,
    MessageReadSerializer,
    MessageSerializer,
)
from chats.permissions import IsChatAdmin, IsChatMember, IsMessageAuthor
from rest_framework import generics


class ChatMessagesQuerySet:
    def get_queryset(self):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chat, pk=chat_pk)
        return chat.chat_messages


class MessageList(ChatMessagesQuerySet, generics.ListAPIView):
    serializer_class = MessageListSerializer
    permission_classes = [IsChatMember]


class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsChatMember]

    def perform_create(self, serializer):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chat, pk=chat_pk)
        serializer.save(chat=chat, author=self.request.user)


class MessageRetrieveUpdateDestroy(
    ChatMessagesQuerySet, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = MessageSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH"]:
            permission_classes = [IsMessageAuthor]
        elif self.request.method == "DELETE":
            permission_classes = [IsMessageAuthor | IsChatAdmin]
        else:
            permission_classes = [IsChatMember]
        return [permission() for permission in permission_classes]


class MessageRead(ChatMessagesQuerySet, generics.UpdateAPIView):
    serializer_class = MessageReadSerializer
    permission_classes = [IsChatMember, ~IsMessageAuthor]
