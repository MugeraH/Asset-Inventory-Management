from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    phone = models.IntegerField()
    bio = models.TextField(default='Bio...📰', max_length=100)
    department= models.ForeignKey('Department',on_delete=models.CASCADE,related_name='asset')

    def __str__(self):
        return f'{self.user.username} Profile'

class User(AbstractBaseUser):
    user_name   = models.CharField(max_length=255, blank=True, null=True)
    email       = models.EmailField(max_length=255, unique=True)
    first_name   = models.CharField(max_length=255, blank=True, null=True)
    last_name   = models.CharField(max_length=255, blank=True, null=True)
    photo       = models.ImageField(verbose_name="vriksh", upload_to="avatars", name="photo", null=True, blank=True)
    # is_active   = models.BooleanField(default=True) # can login 
    # staff       = models.BooleanField(default=False) # staff user non superuser
    Is_admin       = models.BooleanField(default=False) # superuser 
    # timestamp   = models.DateTimeField(auto_now_add=True)

# class User_assets(models.Model):
#     user_id = models.ForeignKey(primary_key=True)
#     asset_id = models.ForeignKey(primary_key=True)