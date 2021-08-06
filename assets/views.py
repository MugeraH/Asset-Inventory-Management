from django.shortcuts import render,reverse,redirect
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from assets.models import Profile 
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

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'assets/profile.html', context)

def profile_page(request):
    profile = Profile.objects.all()
    context = {
       'profile':profile
	}
    return render(request, 'assets/profile_view.html', context)