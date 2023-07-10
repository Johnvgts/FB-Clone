from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from newapp.models import *  

class UserSerializer(serializers.ModelSerializer):
    country = serializers.CharField(max_length=100, write_only=True)
    bio = serializers.CharField(max_length=100, write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'country', 'bio')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'].lower())
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=User.objects.get(pk=user.pk),
                            country=validated_data['country'],
                            bio=validated_data['bio'],)
        return user
        

    def to_representation(self, instance):
        try:
            profile = Profile.objects.get(user=instance.pk)
            friends = Friends.objects.get(from_user=instance.pk)
        except:
            profile = None
            friends = None
        return {
            "id": instance.pk,
            "user": instance.username,
            "bio": profile.bio if profile else None ,
            "profileimg": profile.profileimg.url if profile else None ,
            "country": profile.country if profile else None ,
            "user_count": instance.friends_user.count(),
            "friends": FriendsShowrSerializer(User.objects.filter(pk__in=friends.friends.values_list('pk',flat=True)),many=True).data if friends else [],
        
        } 
    

class FriendsShowrSerializer(serializers.Serializer):
     def to_representation(self, instance):
        profile = Profile.objects.get(user=instance.pk)
        return {
            "id": instance.pk,
            "user": instance.username,
            "bio": profile.bio,
            "profileimg": profile.profileimg.url,
            "country": profile.country,
        } 
