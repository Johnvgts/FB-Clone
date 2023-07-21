from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.generics import RetrieveAPIView,ListAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.AllowAny,)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'


class FriendListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FriendSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Friend.objects.filter(user=self.request.user)

class MessageListCreateView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        receiver_id = self.kwargs['id']
        receiver = get_object_or_404(User, id=receiver_id)
        return Message.objects.filter(sender=self.request.user, receiver=receiver)

    def perform_create(self, serializer):
        receiver_id = self.kwargs['id']
        receiver = get_object_or_404(User, id=receiver_id)
        serializer.save(sender=self.request.user, receiver=receiver)

class UserSearchListAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = User.objects.all()
        if search := self.request.query_params.get('search', None):
            queryset = queryset.filter(username__icontains=search)
        return queryset
    

class FriendSearchByIDAPIView(generics.ListAPIView):
    serializer_class = FriendSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Friend.objects.filter(user=self.request.user, friend_id=user_id)

class MessageSearchByIDAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        receiver_id = self.kwargs['id']
        receiver = get_object_or_404(User, id=receiver_id)
        return Message.objects.filter(sender=self.request.user, receiver=receiver)