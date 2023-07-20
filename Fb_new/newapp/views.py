from django.shortcuts import render
from .serializers import *
from rest_framework import generics, status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import get_user_model


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class FriendsSearchListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
            queryset = User.objects.all()
            if search := self.request.query_params.get('search', False):
                queryset = queryset.filter(username__icontains=search)
            return queryset
    

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # def create(self, request, *args, **kwargs):
    #     sender = request.user
    #     receiver_id = request.data.get('receiver_id', None)

    #     if not receiver_id:
    #         return Response({'error': 'receiver_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

    #     try:
    #         receiver = User.objects.get(pk=receiver_id)
    #     except User.DoesNotExist:
    #         return Response({'error': 'Receiver not found.'}, status=status.HTTP_404_NOT_FOUND)

    #     message_data = {
    #         'sender': sender.id,
    #         'receiver': receiver_id,
    #         'content': request.data.get('content', '')
    #     }
    #     serializer = MessageSerializer(data=message_data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
