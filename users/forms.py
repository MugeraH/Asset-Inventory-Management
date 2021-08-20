    
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


User = get_user_model()
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    firstname=forms.CharField(max_length=254)
    lastname=forms.CharField(max_length=254)
    
    class Meta:
        model = User
        fields = ("username",'firstname','lastname','email',)
