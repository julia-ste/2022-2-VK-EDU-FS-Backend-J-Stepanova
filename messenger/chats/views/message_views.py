from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Chat
from ..serializers import (
    MessageListSerializer,
    MessageReadSerializer,
    MessageSerializer,
)


class ChatMessagesQuerySet:
    def get_queryset(self):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chat, pk=chat_pk)
        return chat.chat_messages


class MessageList(ChatMessagesQuerySet, generics.ListAPIView):
    serializer_class = MessageListSerializer
    permission_classes = (IsAuthenticated,)


class MessageCreate(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chat, pk=chat_pk)
        serializer.save(chat=chat, author=self.request.user)


class MessageRetrieveUpdateDestroy(
    ChatMessagesQuerySet, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)


class MessageRead(ChatMessagesQuerySet, generics.UpdateAPIView):
    serializer_class = MessageReadSerializer
    permission_classes = (IsAuthenticated,)
