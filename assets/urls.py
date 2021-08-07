from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import HomePageView,DashBoardView,employees,employeerequests,employeeassetrequest,employeedetails,assets,requests,requestdetails, update_asset



app_name ="assets"


urlpatterns=[
    

path('',HomePageView,name='home'),
path('employees',views.EmployeesView,name='employees'),
   path('employeedetails/<int:id>', employeedetails,name='employeedetails'),
   
path('dashboard',DashBoardView,name='dashboard'),
path('departments/',views.departments,name='departments'),
path('assets/',views.assets,name='assets'),
path('assets/addasset/',views.asset,name='assetform'),
path('add_department/',views.add_departments,name='departmentform'),
path('update/department/<int:id>/',views.update_department,name='departmentform'),
  
path('update/asset/<int:id>/',views.update_asset,name='assetform'),
path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
path('managerrequest/',views.managerrequest,name='managerrequest'),
path('employeeasset',views.employeeasset,name='employeeasset'),
path('assetassigning/',views.update_asset,name='assetassigning'),
path('departmentassigning/',views.update_department,name='departmentform'),
     path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
    path('managerrequest/',views.managerrequest,name='managerrequest'),
    path('assetdetails/<int:id>', employeedetails,name='assetdetails'),
    path('requests', requests,name='requests'),
    path('requestdetails/<int:id>', requestdetails,name='requestdetails'),




 ]
 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

