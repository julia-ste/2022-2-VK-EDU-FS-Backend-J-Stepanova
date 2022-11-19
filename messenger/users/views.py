from django.contrib.auth import get_user_model

from rest_framework import generics

from .serializers import UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
