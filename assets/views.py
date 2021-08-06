from django.shortcuts import render,reverse,redirect
from django.contrib.auth import login, authenticate
from django.http import Http404,HttpResponse
from . forms import DepartmentForm,AssetForm,EmployeeAssetRequestForm,ManagerRequestForm
from . models import EmployeeAsset,EmployeeAssetRequest,Department
# third party imports

from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from .email import send_welcome_email
import datetime as dt



def HomePageView(request):
    return render(request,'assets/home.html')



def asset(request):
    if request.method == 'POST':
        form=AssetForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('/')
    else:
        form=AssetForm()
    params={
        'form':form,
    }
    return render(request,'assets/addasset.html', params)


def departments(request):
        department=Department.objects.all()
        params={
        'department':department,
        }
        return render(request,'assets/departments.html', params)
def add_departments(request):
    if request.method == 'POST':
        form=DepartmentForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('/')
    else:
        form=DepartmentForm()
    params={
        'form':form,
    }
    return render(request,'assets/adddep.html', params)

def update_department(request, id):
    dept_id = int(id)
    try:
        dept = Department.objects.get(id = dept_id)
    except Department.DoesNotExist:
        return redirect('/')
    form = DepartmentForm(request.POST or None, instance = dept)
    if form.is_valid():
        form.save()
        return redirect('/')
    params={
        'form':form,
    }
    return render(request,'assets/updatedep.html', params)


def employeeassetrequest(request):
    if request.method == 'POST':
        form=EmployeeAssetRequestForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('/')
    else:
        form=EmployeeAssetRequestForm()
    params={
        'form':form,
    }
    return render(request,'assets/employee_request.html', params)

def managerrequest(request):
    if request.method == 'POST':
        form=ManagerRequestForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('/')
    else:
        form=ManagerRequestForm()
    params={
        'form':form,
    }
    return render(request,'assets/manager_request.html', params)

@login_required(login_url='/login')
def DashBoardView(request):
    return render(request,'assets/dashboard.html')

