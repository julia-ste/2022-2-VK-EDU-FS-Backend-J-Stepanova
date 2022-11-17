from rest_framework import serializers

from .models import Chat, Message, ChatMember

ALL_MESSAGE_FIELDS = ["id", "author", "chat", "text", "sent_at", "is_read"]
ALL_CHAT_FIELDS = ["id", "title", "description", "is_group", "author", "category"]


class ChatSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    def create(self, validated_data):
        chat = Chat.objects.create(**validated_data)

        user = validated_data.get("author")
        ChatMember.objects.create(chat=chat, user=user)

        return chat

    class Meta:
        model = Chat
        fields = ALL_CHAT_FIELDS


class ChatListSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    author = serializers.StringRelatedField()

    def create(self, validated_data):
        chat = Chat.objects.create(**validated_data)

        user = validated_data.get("author")
        ChatMember.objects.create(chat=chat, user=user)

        return chat

    class Meta:
        model = Chat
        fields = ["title", "description", "author"]


class ChatMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMember
        fields = ["chat", "user"]


class MessageSerializer(serializers.ModelSerializer):
    chat = serializers.StringRelatedField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ALL_MESSAGE_FIELDS


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
    class Meta:
        model = Message
        fields = ["author", "chat", "text"]
