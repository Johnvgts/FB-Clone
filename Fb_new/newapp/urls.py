from django.urls import path
from . import views
from rest_framework.authtoken import views as authtoken

urlpatterns = [
    path('user_create/', views.UserCreateAPIView.as_view()),
    path('users/<int:id>/',views.UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('friends/',views.FriendListCreateAPIView.as_view(), name='friend-list-create'),
    path('messages/<int:id>/',views.MessageListCreateView.as_view(), name='message-list-create'),
    path('users/search/',views.UserSearchListAPIView.as_view(), name='user-search'),
    path('friends/search_id/<int:id>/',views.FriendSearchByIDAPIView.as_view(), name='friend-search-id'),
    path('messages/search_id/<int:id>/',views.MessageSearchByIDAPIView.as_view(), name='message-search-id'),




]   