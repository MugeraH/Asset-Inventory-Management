from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.


class Profile(models.Model):
    employee=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    image=models.ImageField(upload_to='profile-pics',default='default.jpeg')

    def __str__(self):
        return f'{self.employee.username}- Profile'

