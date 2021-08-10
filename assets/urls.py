from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import HomePageView,DashBoardView,employees,employeerequests,employeeassetrequest,employeedetails,assets,assetdetails,addasset
addasset


app_name ="assets"


urlpatterns=[
    
    path('',HomePageView,name='home'),
    path('forms/',views.departments,name='forms'),
    path('update/department/<int:id>/',views.update_department,name='update_department'),
    path('departments/',views.departments,name='departments'), 
    path('addasset',views.addasset,name='assetform'),
    path('add_department/',views.add_departments,name='departmentform'),
    path('employees', views.employees,name='employees'),
    
    path('employeeassetrequest',views.employeeassetrequest,name='employeeassetrequest'),
    path('managerrequest/',views.managerrequest,name='managerrequest'),
    path('assetdetails/<int:id>', views.assetdetails,name='assetdetails'),
    path('delete/<int:id>/', views.delete_asset,name='delete_asset'),
    path('employees',views.employees,name='employees'),
    path('employeedetails/<int:id>', employeedetails,name='employeedetails'),

    path('dashboard',DashBoardView,name='dashboard'),
    path('employeedetails/<int:id>', views.employeedetails,name='employeedetails'),
    path('department_detail/<int:id>',views.department_detail,name='department_detail'),
    path('assets/',views.assets,name='assets'),

    path('update/asset/<int:id>/',views.update_asset,name='assetform'),
    path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
    path('employeeasset',views.employeeasset,name='employeeasset'),
    path('assign_asset/<int:id>',views.assign_asset,name='assign_asset'),

    path('requests', views.requests,name='requests'),
    path('requestdetails/<int:id>', views.requestdetails,name='requestdetails'),
    path('add_departments/',views.add_departments,name='add_departments'),



path('employees',views.employees,name='employees'),
path('dept_employees',views.dept_employees,name='dept_employees'),
path('employee_assets',views.employee_assets,name='employee_assets'),


path('dashboard',DashBoardView,name='dashboard'),
path('manager_dashboard',views.managerDashBoardView,name='manager_dashboard'),
path('employee_dashboard',views.employeeDashBoardView,name='employee_dashboard'),

path('employeedetails/<int:id>', views.employeedetails,name='employeedetails'),



path('department_detail/<int:id>',views.department_detail,name='department_detail'),
path('assets/',views.assets,name='assets'),
path('dept_assets/',views.dept_assets,name='dept_assets'),

path('update/asset/<int:id>/',views.update_asset,name='assetform'),
path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),

path('assign_asset/<int:id>',views.assign_asset,name='assign_asset'),
path('assign_asset_user/<int:id>',views.assign_asset_user,name='assign_asset_user'),
path('unassign_asset_user/<int:id>',views.unassign_asset_user,name='unassign_asset_user'),

path('requests', views.requests,name='requests'),
path('requestdetails/<int:id>', views.requestdetails,name='requestdetails'),




]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

