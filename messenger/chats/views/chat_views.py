from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from chats.models import Chat, ChatMember
from chats.serializers import ChatListSerializer, ChatMemberSerializer, ChatSerializer
from rest_framework import generics


class UserChatsQuerySet:
    def get_queryset(self):
        return Chat.objects.filter(author=self.request.user)


class ChatList(UserChatsQuerySet, generics.ListAPIView):
    serializer_class = ChatListSerializer


class ChatCreate(generics.CreateAPIView):
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ChatRetrieveUpdateDestroy(
    UserChatsQuerySet, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ChatSerializer


class ChatMemberCreate(generics.CreateAPIView):
    serializer_class = ChatMemberSerializer

    def perform_create(self, serializer):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chat, pk=chat_pk)
        serializer.save(chat=chat)


class ChatMemberDestroy(generics.DestroyAPIView):
    serializer_class = ChatMemberSerializer
    lookup_field = "chat_id"
    lookup_url_kwarg = "chat_pk"

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")
        user = get_object_or_404(get_user_model(), pk=user_pk)
        return ChatMember.objects.filter(user=user)
