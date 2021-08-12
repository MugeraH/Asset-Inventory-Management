from django.db.models import manager
from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import Http404,HttpResponse

from . forms import DepartmentForm,AssetForm,EmployeeAssetRequestForm,ManagerRequestForm,AssetAssigningForm,DepartmentAssigningForm,EmployeeProfile,EmployeeRequest,ManagerRequestUpdateForm
from . forms import DepartmentForm,AssetForm,EmployeeAssetRequestForm,ManagerRequestForm,AssetAssigningForm,DepartmentAssigningForm,EmployeeProfile
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
     
        if request.user.is_admin:
            return redirect('assets:manager_dashboard')
        
        if not request.user.is_admin and not request.user.is_superuser:
            return redirect('assets:employee_dashboard')
       
       
        
        total_asset = Asset.objects.count()
        total_department = Department.objects.count()
        total_user = User.objects.count()      
       
        context = {
        'assets': total_asset,
        'departments': total_department,
        
        'employees' : total_user,
    
        
        }
        return render(request,'assets/dashboard.html',context)
def  employeeDashBoardView(request):
       
     
        asset = EmployeeAsset.objects.filter(employee__user=request.user.id) 
          
        context = {
        'asset': asset,        
        }
        return render(request,'assets/employee_dashboard.html',context)
    
def  managerDashBoardView(request):
        user=Profile.objects.get(user=request.user)
        manager_requests= ManagerRequest.objects.filter(employee=user)
        department= Department.objects.get(manager=request.user.id)
        
        dept_assets=Asset.objects.filter(department=department)
        dept_employees=Profile.objects.filter(department=department)
       
         
       
        context = {
    
        'department':department,
      'manager_requests':manager_requests,
       'dept_assets':dept_assets,
       'dept_employees': dept_employees
        
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

def assets(request):
    if request.user.is_admin:
            return redirect('assets:dept_assets')
        
    if not request.user.is_admin and not request.user.is_superuser:
            return redirect('assets:employee_assets')
    
    assets=Asset.objects.all()
    user=User.objects.get(id=request.user.id)
    print(user)
    form=AssetForm()
    if request.method == 'POST':
        form=AssetForm(request.POST,request.FILES)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('assets:assets')
    else:
        form=AssetForm()
    
    params= {'assets': assets,'form':form,'user':user}
    return render(request,'assets/assets.html', params)

def dept_assets(request):
   
    department= Department.objects.get(manager=request.user.id)
    dept_assets=EmployeeAsset.objects.filter(asset__department=department)
    
    
    user=User.objects.get(id=request.user.id)
    print(dept_assets)
  
    
    params= {'dept_assets': dept_assets,'user':user}
    return render(request,'assets/departmentAsset.html',params)

def employee_assets(request):
    assets = EmployeeAsset.objects.filter(employee__user=request.user.id) 
           
    context = {
        'assets': assets,        
        }
    return render(request,'assets/employee_assets.html', context)





def assetdetails(request,id):
    asset=Asset.objects.get(id=id)
    params={
        'asset':asset,
        
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

def assign_asset(request,id):
    asset=Asset.objects.get(id=id)
    form =AssetAssigningForm(instance = asset)
    if request.method == 'POST':
        form=AssetAssigningForm(request.POST,instance = asset)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.is_assigned_dept = True
            asset.save()
            return redirect('assets:assetdetails',id=id)
    else:
        form=AssetAssigningForm()

    params={
        'form':form,
        'asset':asset
    }
    return render(request,'assets/assignasset.html', params)

def assign_asset_user(request,id):
    asset= EmployeeAsset.objects.get(asset_id=id)
    assigned_asset=Asset.objects.get(id=id)
    employees = Profile.objects.filter(department=asset.asset.department)
   
  
    if request.method == 'POST':
        
            name= request.POST.get('employee')
            employee = Profile.objects.get(user__username=name)
            print(employee)
            assigned_asset.is_assigned_user=True
            assigned_asset.save()
            
            asset.employee=employee
            asset.save()
          
            return redirect('assets:dept_assets')
    else:
        print('')

    params={
       'employees':employees,
        'asset':asset
    }
    return render(request,'assets/assignuserasset.html', params)

def unassign_asset_user(request,id):
    asset= EmployeeAsset.objects.get(asset_id=id)
    assigned_asset=Asset.objects.get(id=id)
       
    assigned_asset.is_assigned_user=False
    assigned_asset.save()
            
    asset.employee=None
    asset.save()
          
    return redirect('assets:dept_assets')
def unassign_asset_dept(request,id):
    
    try:
        asset= EmployeeAsset.objects.get(asset_id=id)
    except Asset.DoesNotExist:
        print("")
   
    assigned_asset=Asset.objects.get(id=id)
       
    assigned_asset.is_assigned_user=False
    assigned_asset.is_assigned_dept=False
    assigned_asset.department=None
    assigned_asset.save()
            
    asset.employee=None
    asset.save()
          
    return redirect('assets:assets')
  

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
        employees= Profile.objects.filter(department=department)
        assets=Asset.objects.filter(department=department)
        form = DepartmentForm(instance=department)
        if request.method == "POST":
            form = DepartmentForm(request.POST or None, instance = department)
            if form.is_valid():
                form.save()
                return redirect('assets:department_detail', id)
        context={
        'department': department,
         'form':form,
         'assets':assets,
         'employees':employees
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
    if request.user.is_admin:
            return redirect('assets:dept_employees')
    employees= Profile.objects.all()

    params={
        'employees':employees,
    }
    return render(request,'assets/employees.html', params)

def dept_employees(request):
    department= Department.objects.get(manager=request.user.id)
    employees= Profile.objects.filter(department=department)

    params={
        'employees':employees,
    }
    return render(request,'assets/employees.html', params)



@login_required(login_url='/login')
def employeedetails(request,id):
    employee= Profile.objects.get(id=id)
    user = User.objects.get(id=id)
    # asset=EmployeeAsset.objects.filter(employee=employee.user)
    # requests=EmployeeAssetRequest.objects.filter(employee=employee.user)
    
    form = EmployeeProfile(instance = employee)
    
    
    
    if request.method == 'POST':
        form= EmployeeProfile(request.POST,instance = employee)
      
        if form.is_valid() :
        
            dept = form.cleaned_data['department']
            
           
            department = Department.objects.get(name=dept)
            role = form.cleaned_data['role']
            if role == "Admin":
                department.manager=user
                department.save()
                user.is_admin=True
                user.save()
            else:
                department.manager=None
                department.save()
                user.is_admin=False
                user.save()
           
            form.save()
            return redirect('assets:employeedetails',id=id)
   

    params={
        'employee': employee,
        # 'asset': asset,
        # 'requests': requests,
        'form': form,
       
    }
    return render(request,'assets/employeedetails.html', params)
@login_required(login_url='/login')
def employeerequests(request):
    assets= EmployeeAssetRequest.objects.all()

    params= {'assets': assets,}

    return render(request,'assets/employee_request.html', params)



@login_required(login_url='/login')
def employeeassetrequest(request):
    if request.method == 'POST':
        form=EmployeeAssetRequestForm(request.POST,request.FILES)
        if form.is_valid():
            request = form.save(commit=False)
            # request.employee=request.profile
            request.save()
            return redirect('/')    
    else:
        form=EmployeeAssetRequestForm()
    params={
        'form':form,
    }
    return render(request,'assets/employee_request.html', params)

@login_required(login_url='/login')
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
    if request.user.is_admin:
            return redirect('assets:dept_requests')
        
    if not request.user.is_admin and not request.user.is_superuser:
            return redirect('assets:employee_requests')

    emp_requests=EmployeeAssetRequest.objects.all()
    manager_requests= ManagerRequest.objects.all()


    employee=Profile.objects.get(user=request.user.id)
    my_requests_manager=ManagerRequest.objects.filter(employee=employee)
    my_requests_employee=EmployeeAssetRequest.objects.filter(employee=employee)

  
    form=ManagerRequestForm()
    if request.method == 'POST':
        form=ManagerRequestForm(request.POST,request.FILES)
       
        if form.is_valid():
            request = form.save(commit=False)
            request.save()
            return redirect('assets:requests')
    else:
        form=ManagerRequestForm()   
            
    params={
        'manager_requests':manager_requests,
        'form':form,
        'emp_requests':emp_requests,
        # 'dept_requests':dept_requests,

        'my_requests_man':my_requests_manager,
        'my_requests_emp':my_requests_employee
    }
    return render(request,'assets/requests.html',params)

####################

def dept_requests(request):
   
   
    department= Department.objects.get(manager=request.user.id)
    print(department)
    
    dept_requests=EmployeeAssetRequest.objects.filter(employee__department=department)
    
    user=Profile.objects.get(user=request.user)
    my_requests= ManagerRequest.objects.filter(employee=user)
    
    print(user)

    form=ManagerRequestForm()
    if request.method == 'POST':
        form=ManagerRequestForm(request.POST,request.FILES)
       
        if form.is_valid():
            request = form.save(commit=False)
            request.employee=user
        
            request.save()
            return redirect('assets:dept_requests')
    else:
        form=ManagerRequestForm()
  
    
    params= {
        'my_requests':my_requests,
        'dept_requests': dept_requests,

        'user':user,
        'form':form,
    }
    return render(request,'assets/departmentRequest.html',params)


def employee_requests(request):
    

    user=request.user.id
    # employee=Profile.objects.get(user=user)
    # requests=EmployeeAssetRequest.objects.get(employee=employee)
    # user=User.objects.get(id=request.user.id)
    # print(dept_requests)
    user=Profile.objects.get(user=request.user)
    requests=EmployeeAssetRequest.objects.filter(employee=user)
    form=EmployeeAssetRequestForm()
    if request.method == 'POST':
        form=EmployeeAssetRequestForm(request.POST,request.FILES)
       
        if form.is_valid():
            request = form.save(commit=False)
            request.employee = user
            request.save()
            return redirect('assets:employee_requests')
    else:
        form=EmployeeAssetRequestForm()
    params = {
        'requests':requests,
        'user':user,
        'form':form
    }


    return render(request,'assets/employeeRrequests.html',params)






##########################









@login_required(login_url='/login')
def employeerequestdetails(request,id):
   
    employee_requests=EmployeeAssetRequest.objects.get(id=id)
   
    status= get_object_or_404(EmployeeAssetRequest,id=id)
    form = EmployeeRequest()
        
    if request.method == 'POST':
            form= EmployeeRequest(request.POST or None,instance = status)
        
            if form.is_valid() :
                                
                form.save()
                return redirect('assets:employeerequestdetails',id=id)

    params={
      
        'employee_requests': employee_requests,
        'form': form,
    }
    return render(request,'assets/employeerequestdetails.html', params)

@login_required(login_url='/login')
def managerrequestdetails(request,id):
    manager_requests= ManagerRequest.objects.get(id=id)
    # user = User.objects.get(id=id)
    status= get_object_or_404(ManagerRequest,id=id)
    form = ManagerRequestUpdateForm()
            
    if request.method == 'POST':
                form= ManagerRequestUpdateForm(request.POST or None,instance = status)
            
                if form.is_valid() :
                                    
                    form.save()
                    return redirect('assets:managerrequestdetails',id=id)

    params={
        'manager_requests': manager_requests,
        'form': form,
    }


    return render(request,'assets/managerrequestdetails.html', params)



@login_required(login_url='/login')
def delete_asset(request, id):
    id = int(id)
    try:
        asset = Asset.objects.get(id = id)
    except Asset.DoesNotExist:
        return redirect(request,'assets/assets.html')
    asset.delete()
    return redirect(request,'assets/assets.html')

