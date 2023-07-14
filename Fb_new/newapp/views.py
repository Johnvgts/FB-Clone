from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class FriendsSearchListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer


    def get_queryset(self):
            queryset = User.objects.all()
            if search := self.request.query_params.get('search', False):
                queryset = queryset.filter(username__icontains=search)
            return queryset