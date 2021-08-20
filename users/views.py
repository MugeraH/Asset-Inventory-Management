from django.shortcuts import render,redirect,reverse

from django.views import generic 
from .forms import CustomUserCreationForm
from .email import send_welcome_email
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
import datetime as dt

from django.contrib.auth.mixins import LoginRequiredMixin



# class SignupView(generic.CreateView):
#     template_name = 'registration/signup.html'
#     form_class = CustomUserCreationForm

#     def get_success_url(self):
#         return reverse("login")
    
def SignupView(request):
    date = dt.date.today()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            name=username
            email=form.cleaned_data['email']
            send_welcome_email(name,email,date)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def HomePageView(request):
  
    return render(request,'users/home.html')
