from chats.models import ChatMember
from rest_framework import permissions


class IsChatOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsMessageAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsChatAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        chat_pk = view.kwargs.get("chat_pk")
        chat_member = ChatMember.objects.filter(
            chat_id=chat_pk, user=request.user
        ).first()
        return bool(chat_member and chat_member.is_admin)


class IsChatMember(permissions.BasePermission):
    def has_permission(self, request, view):
        chat_pk = view.kwargs.get("chat_pk")
        is_chat_member = ChatMember.objects.filter(
            chat_id=chat_pk, user=request.user
        ).exists()
        return is_chat_member
