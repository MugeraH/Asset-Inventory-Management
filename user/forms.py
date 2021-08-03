from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CreateUserForm(UserCreationForm):
    email=forms.EmailField()

    class meta:
        models= User
        field= ['username','email','password1', 'password2']

