from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100,blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username   
    

class Friends(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_user')
    friends = models.ManyToManyField(User)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.content}"