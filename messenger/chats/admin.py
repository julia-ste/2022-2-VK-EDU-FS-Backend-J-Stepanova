from django.contrib import admin

from chats.models import Category, Chat, ChatMember, Message


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class ChatAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class ChatMemberAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(ChatMember, ChatMemberAdmin)
admin.site.register(Message, MessageAdmin)
