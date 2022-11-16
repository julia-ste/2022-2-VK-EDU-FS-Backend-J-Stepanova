from django.urls import path

from chats.views import chat_views
from chats.views import message_views

urlpatterns = [
    path("<int:user_pk>/", chat_views.chat_list, name="chat_list"),
    path("new/", chat_views.chat_create, name="chat_create"),
    path("detail/<int:pk>/", chat_views.chat_detail, name="chat_detail"),
    path("update/<int:pk>/", chat_views.chat_update, name="chat_update"),
    path("delete/<int:pk>/", chat_views.chat_delete, name="chat_delete"),
    path("add-member/<int:chat_pk>/", chat_views.chat_add_member, name="chat_add_member"),
    path("delete-member/<int:chat_pk>/", chat_views.chat_delete_member, name="chat_delete_member"),

    path("messages/<int:chat_pk>/", message_views.message_list, name="message_list"),
    path("messages/<int:chat_pk>/new/", message_views.message_create, name="message_create"),
    path("messages/detail/<int:pk>", message_views.message_detail, name="message_detail"),
    path("messages/update/<int:pk>", message_views.message_update, name="message_update"),
    path("messages/delete/<int:pk>", message_views.message_delete, name="message_delete"),
    path("messages/read/<int:pk>", message_views.message_delete, name="message_read"),
]
