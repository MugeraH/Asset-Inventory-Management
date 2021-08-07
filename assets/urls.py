from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import HomePageView,DashBoardView, update_asset


app_name ="assets"


urlpatterns=[
    
path('',HomePageView,name='home'),
path('employees',views.EmployeesView,name='employees'),
path('dashboard',DashBoardView,name='dashboard'),
path('departments/',views.departments,name='departments'),
path('assets/',views.assets,name='assets'),
path('asset/',views.asset,name='assetform'),
path('department/',views.add_departments,name='departmentform'),
path('update/department/<int:id>/',views.update_department,name='departmentform'),
path('update/asset/<int:id>/',views.update_asset,name='assetform'),
path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
path('managerrequest/',views.managerrequest,name='managerrequest'),
path('employeeasset',views.employeeasset,name='employeeasset'),
path('assetassigning/',views.update_asset,name='assetassigning'),
path('departmentassigning/',views.update_department,name='departmentform'),



 ]
 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

