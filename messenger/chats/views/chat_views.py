from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics

from chats.models import Chat, ChatMember
from chats.serializers import ChatSerializer, ChatListSerializer, ChatMemberSerializer


class ChatList(generics.ListAPIView):
    serializer_class = ChatListSerializer

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")
        user = get_object_or_404(get_user_model(), pk=user_pk)

        return ChatMember.objects.filter(user=user)


class ChatCreate(generics.CreateAPIView):
    serializer_class = ChatSerializer


class ChatRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatMemberCreate(generics.CreateAPIView):
    serializer_class = ChatMemberSerializer
