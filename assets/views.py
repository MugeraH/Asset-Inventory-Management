from django.shortcuts import render,reverse,redirect
from django.contrib.auth import login, authenticate
from django.http import Http404,HttpResponse

# third party imports

from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from .email import send_welcome_email
import datetime as dt



def HomePageView(request):
  
    return render(request,'assets/home.html')

@login_required(login_url='/login')
def DashBoardView(request):
    
  
    return render(request,'assets/dashboard.html')
