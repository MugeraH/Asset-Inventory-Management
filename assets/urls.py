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

   
path('dashboard',DashBoardView,name='dashboard'),

path('employeedetails/<int:id>', views.employeedetails,name='employeedetails'),



path('department_detail/<int:id>',views.department_detail,name='department_detail'),
path('assets/',views.assets,name='assets'),




path('update/asset/<int:id>/',views.update_asset,name='assetform'),
path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
path('employeeasset',views.employeeasset,name='employeeasset'),
path('assign_asset/<int:id>',views.assign_asset,name='assign_asset'),
path('departmentassigning/',views.update_department,name='departmentform'),




path('requests', views.requests,name='requests'),
path('requestdetails/<int:id>', views.requestdetails,name='requestdetails'),








path('add_departments/',views.add_departments,name='add_departments'),




]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

