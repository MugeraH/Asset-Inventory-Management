from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import HomePageView,DashBoardView


app_name ="assets"


urlpatterns=[
    
path('',HomePageView,name='home'),
path('employees',views.EmployeesView,name='employees'),
path('dashboard',DashBoardView,name='dashboard'),
path('forms/',views.departments,name='forms'),
path('update/department/<int:id>/',views.update_department,name='update_department'),
path('departments/',views.departments,name='departments'),
path('asset/',views.asset,name='assetform'),
path('department/',views.add_departments,name='departmentform'),
path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
path('managerrequest/',views.managerrequest,name='managerrequest'),




 ]
 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

