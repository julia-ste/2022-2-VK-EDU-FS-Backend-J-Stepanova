from django.shortcuts import get_object_or_404
from rest_framework import generics

from chats.models import Chat, Message
from chats.serializers import MessageListSerializer, MessageSerializer, MessageReadSerializer


class MessageList(generics.ListAPIView):
    serializer_class = MessageListSerializer

    def get_queryset(self):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chat, pk=chat_pk)

        return chat.chat_messages


class MessageCreate(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageRead(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageReadSerializer
