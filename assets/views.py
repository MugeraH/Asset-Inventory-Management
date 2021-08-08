from django.shortcuts import render,reverse,redirect
from django.contrib.auth import login, authenticate
from django.http import Http404,HttpResponse

from . forms import DepartmentForm,AssetForm,EmployeeAssetRequestForm,ManagerRequestForm,EmployeeAssetForm,AssetAssigningForm,DepartmentAssigningForm
from . models import EmployeeAsset,EmployeeAssetRequest,Department,Asset,ManagerRequest,Profile

import sys
sys.path.append("..")
from users.models import User
# third party imports

from django.views import generic 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# from .email import send_welcome_email
import datetime as dt


def HomePageView(request):
    return render(request,'assets/home.html')

def  DashBoardView(request):
        total_asset = Asset.objects.count()
        total_department = Department.objects.count()
        total_user = User.objects.count()
        dept_employees=User.objects.count()
        dept_assets=Asset.objects.count()
        context = {
        'assets': total_asset,
        'departments': total_department,
        'employees' : total_user,
        'dept_employees':dept_employees,
        'dept_assets':dept_assets
        
        }
        return render(request,'assets/dashboard.html',context)



def addasset(request):
   
    if request.method == 'POST':
        form=AssetForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('assets:assets')
    else:
        form=AssetForm()
    params={
        'form':form
    }
    return render(request,'assets/addasset.html', params)

# def assets(request):
#     asset=Asset.objects.all()
#     form = AssetForm()
#     if request.method == 'POST':
#         form=AssetForm(request.POST,request.FILES)
#     if form.is_valid():   
#         asset = form.save(commit=False)
#         asset.save()
#         return redirect('assets:assets')
#     else:
#         form=AssetForm()    

#     params={
#           'asset':asset,
#            'form':form
#       }
#     return render(request,'assets/assets.html', params)

def assetdetails(request,id):
    asset=Asset.objects.get(id=id)
    params={
        'asset':asset
    }

    return render(request,'assets/assetdetails.html', params)

def update_asset(request, id):
    asset_id = int(id)
    try:
        asset = Asset.objects.get(id = asset_id)
    except Asset.DoesNotExist:
        return redirect('/')
    form = AssetForm(request.POST or None, instance = asset)
    if form.is_valid():
       form.save()
       return redirect('/')

    asset=Asset.objects.all()
    params={
        'asset':asset,
    }
    return render(request,'assets/assets.html', params)

def asign_asset(request):
    if request.method == 'POST':
        form=DepartmentAssigningForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('/')
    else:
        form=AssetAssigningForm()

    params={
        'form':form,
    }
    return render(request,'assets/employeedetails.html', params)
    

def departments(request):
        department=Department.objects.all()
        form = DepartmentForm()
        if request.method == 'POST':
            form=DepartmentForm(request.POST,request.FILES)
        if form.is_valid():
                asset = form.save(commit=False)
                asset.save()
                return redirect('assets:departments')
        else:
            form=DepartmentForm()
   
        params={
        'department':department,
         'form':form,
        }
        return render(request,'assets/departments.html', params)

def department_detail(request,id):
        form = DepartmentForm()
        department=Department.objects.get(id=id)
        form = DepartmentForm(instance=department)
        if request.method == "POST":
            form = DepartmentForm(request.POST or None, instance = department)
            if form.is_valid():
                form.save()
                return redirect('assets:department_detail', id)
        context={
        'department': department,
         'form':form,
        }
        return render(request,'assets/depdetails.html', context)

def add_departments(request):
    if request.method == 'POST':
        form=DepartmentForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('assets:departments')
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
        return redirect('assets:department_detail', id)
    params={
        'form':form,
    }
    return render(request,'assets/apdatedep.html', params)



def employees(request):
    employees= User.objects.all()

    params={
        'employees':employees,
    }
    return render(request,'assets/employees.html', params)

@login_required(login_url='/login')
def employeedetails(request,id):
    employee= User.objects.get(id=id)
    asset=EmployeeAsset.objects.filter(employee=employee)
    requests=EmployeeAssetRequest.objects.filter(employee=employee)

    params={
        'employee': employee,
        'asset': asset,
        'requests': requests
    }
    return render(request,'assets/employeedetails.html', params)

# def employee_assets(request):
#     assets= EmployeeAsset.objects.all()

#     params= {'assets': assets}
#     return render(request,'assets/employee_assets.html', params)


def employeerequests(request):
    assets= EmployeeAssetRequest.objects.all()

    params= {'assets': assets,}

    return render(request,'assets/employee_request.html', params)

def assets(request):
    assets=Asset.objects.all()
    params= {'assets': assets}
    return render(request,'assets/assets.html', params)


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

def delete_employee(request, id):
    id = int(id)
    try:
        employee = User.objects.get(id = id)
    except Asset.DoesNotExist:
        return redirect(request,'assets/employees.html')
    employee.delete()
    return redirect(request,'assets/employees.html')
@login_required(login_url='/login')
def requests(request):
    requests= ManagerRequest.objects.all()
    params={
        'requests':requests,
    }
    return render(request,'assets/requests.html',params)

@login_required(login_url='/login')
def requestdetails(request,id):
    requests= ManagerRequest.objects.get(id=id)
    print(requests)
    params={
        'requests': requests
    }
    return render(request,'assets/requestdetails.html', params)



def employeeasset(request):
    if request.method == 'POST':
        form=EmployeeAssetForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('/')
    else:
        form=EmployeeAssetForm()
    params={
        'form':form,
    }
    return render(request,'assets/employee_asset.html', params)


def delete_asset(request, id):
    id = int(id)
    try:
        asset = Asset.objects.get(id = id)
    except Asset.DoesNotExist:
        return redirect(request,'assets/assets.html')
    asset.delete()
    return redirect(request,'assets/assets.html')