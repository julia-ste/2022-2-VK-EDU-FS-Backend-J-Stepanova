from django.http import Http404

from rest_framework import serializers

from .models import Chat, ChatMember, Message

ALL_MESSAGE_FIELDS = ["id", "author", "chat", "text", "sent_at", "is_read"]
ALL_CHAT_FIELDS = ["id", "title", "description", "is_group", "author", "category"]


class ChatSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    def create(self, validated_data):
        chat = Chat.objects.create(**validated_data)

        user = validated_data.get("author")
        ChatMember.objects.create(chat=chat, user=user, is_admin=True)

        return chat

    class Meta:
        model = Chat
        fields = ALL_CHAT_FIELDS
        read_only_fields = ["id", "author"]


class ChatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["id", "title", "description"]
        read_only_fields = ["id"]


class ChatMemberSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data.get("user")
        chat = validated_data.get("chat")

        chat_member = ChatMember.objects.filter(chat=chat, user=user).first()
        if chat_member:
            raise Http404(f"User {user} already in chat {chat}!")

        return ChatMember.objects.create(**validated_data)

    class Meta:
        model = ChatMember
        fields = ["chat", "user"]
        read_only_fields = ["chat"]


class MessageSerializer(serializers.ModelSerializer):
    chat = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ALL_MESSAGE_FIELDS
        read_only_fields = ["id", "is_read"]


class MessageReadSerializer(serializers.ModelSerializer):
    chat = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    def update(self, instance, validated_data):
        instance.is_read = True
        instance.save()
        return instance

    class Meta:
        model = Message
        fields = ALL_MESSAGE_FIELDS
        read_only_fields = ALL_MESSAGE_FIELDS


class MessageListSerializer(serializers.ModelSerializer):
    chat = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ["id", "author", "chat", "text"]
        read_only_fields = ["id"]
