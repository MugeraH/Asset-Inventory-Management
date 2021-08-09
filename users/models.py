from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username   = models.CharField(max_length=255, unique=True)
    email       = models.EmailField(max_length=255, unique=True)
    firstname   = models.CharField(max_length=255, unique=True)
    lastname   = models.CharField(max_length=255, unique=True)
    is_admin       = models.BooleanField(default=False) 
    
    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = []
    
    
    class Meta:
        ordering = ["pk"]

    