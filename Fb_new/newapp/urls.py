from django.urls import path
from . import views
from rest_framework.authtoken import views as authtoken

urlpatterns = [
    path('api_login/',authtoken.obtain_auth_token),
    path('user_create/', views.UserCreateAPIView.as_view()),
    path('search/friends/', views.FriendsSearchListAPIView.as_view(), name='friend-search'),


]