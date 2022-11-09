from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_pk>/', views.chat_list, name='chat_list'),
    path('new/', views.chat_create, name='chat_create'),
    path('detail/<int:pk>/', views.chat_detail, name='chat_detail'),
    path('update/<int:pk>/', views.chat_update, name='chat_update'),
    path('delete/<int:pk>/', views.chat_delete, name='chat_delete'),

    path("messages/<int:chat_pk>/", views.message_list, name="message_list"),
    path("messages/<int:chat_pk>/new/", views.message_create, name="message_create"),
    path("messages/detail/<int:pk>", views.message_detail, name="message_detail"),
    path("messages/update/<int:pk>", views.message_update, name="message_update"),
    path("messages/delete/<int:pk>", views.message_delete, name="message_delete"),
]
