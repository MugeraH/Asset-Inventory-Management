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
    path('employees', employees,name='employees'),
    # path('employee_assets', views.employee_assets,name='employee_assets'),
    path('employeerequests', employeeassetrequest,name='employeerequests'),
    path('employeedetails/<int:id>', employeedetails,name='employeedetails'),
    path('dashboard',DashBoardView,name='dashboard'),
    path('assets',assets, name='assets'),
    path('updateasset/<int:id>/',views.update_asset,name='updateasset'),
    path('employeeassetrequest',views.employeeassetrequest,name='employeeassetrequest'),
    path('managerrequest/',views.managerrequest,name='managerrequest'),
    path('assetdetails/<int:id>', views.assetdetails,name='assetdetails'),
    path('delete/<int:id>/', views.delete_asset,name='delete_asset'),


path('',HomePageView,name='home'),
path('employees',views.employees,name='employees'),
path('employeedetails/<int:id>', employeedetails,name='employeedetails'),
   
path('dashboard',DashBoardView,name='dashboard'),
path('employeedetails/<int:id>', views.employeedetails,name='employeedetails'),

path('dashboard',views.DashBoardView,name='dashboard'),
path('departments/',views.departments,name='departments'),
path('department_detail/<int:id>',views.department_detail,name='department_detail'),
path('assets/',views.assets,name='assets'),

path('add_department/',views.add_departments,name='departmentform'),


path('update/asset/<int:id>/',views.update_asset,name='assetform'),
path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
path('employeeasset',views.employeeasset,name='employeeasset'),
path('assetassigning/',views.update_asset,name='assetassigning'),
path('departmentassigning/',views.update_department,name='departmentform'),
path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
path('managerrequest/',views.managerrequest,name='managerrequest'),
path('assetdetails/<int:id>', views.employeedetails,name='assetdetails'),

path('requests', views.requests,name='requests'),
path('requestdetails/<int:id>', views.requestdetails,name='requestdetails'),



path('update/department/<int:id>/',views.update_department,name='update_department'),




path('add_departments/',views.add_departments,name='add_departments'),




]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

