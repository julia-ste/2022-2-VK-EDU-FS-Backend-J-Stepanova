from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('<int:pk>/', views.chat_detail, name='chat_detail'),
    path('new/', views.chat_create, name='chat_create'),
]
