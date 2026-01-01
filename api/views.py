from django.shortcuts import render
from .serializers import TodoSerializer, UserSerializer
from rest_framework import viewsets
from todo.models import Todo
from django.contrib.auth.models import User

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all().order_by("-created")


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by("-date_joined")
