from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Chat, ChatMember
from ..serializers import ChatListSerializer, ChatMemberSerializer, ChatSerializer


class UserChatsQuerySet:
    def get_queryset(self):
        return Chat.objects.filter(author=self.request.user)


class ChatList(UserChatsQuerySet, generics.ListAPIView):
    serializer_class = ChatListSerializer
    permission_classes = (IsAuthenticated,)


class ChatCreate(generics.CreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ChatRetrieveUpdateDestroy(
    UserChatsQuerySet, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)


class ChatMemberCreate(generics.CreateAPIView):
    serializer_class = ChatMemberSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        chat_pk = self.kwargs.get("chat_pk")
        chat = get_object_or_404(Chat, pk=chat_pk)
        serializer.save(chat=chat)


class ChatMemberDestroy(generics.DestroyAPIView):
    serializer_class = ChatMemberSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "chat_id"
    lookup_url_kwarg = "chat_pk"

    def get_queryset(self):
        user_pk = self.kwargs.get("user_pk")
        user = get_object_or_404(get_user_model(), pk=user_pk)
        return ChatMember.objects.filter(user=user)
