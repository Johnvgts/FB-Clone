from django.contrib import admin
from django.db import models
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Profile)
admin.site.register(Friends)
admin.site.register(Message)