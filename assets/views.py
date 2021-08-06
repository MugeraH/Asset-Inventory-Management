from django.shortcuts import render,reverse,redirect
from django.contrib.auth import login, authenticate
from django.http import Http404,HttpResponse
from .models import Asset, Department
import sys
sys.path.append("..")
from users.models import User


# third party imports

from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from .email import send_welcome_email
import datetime as dt


# @login_required(login_url='/login')
def HomePageView(request):
  
    return render(request,'assets/home.html')

@login_required(login_url='/login')
def DashBoardView(request):
        total_asset = Asset.objects.count()
        total_department = Department.objects.count()
        total_user = User.objects.count()
        context = {
        
        'asset': total_asset,
        'department': total_department,
        'user' : total_user
    
        

        }
        return render(request,'assets/dashboard.html',context)