from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import HomePageView,DashBoardView,employees,employeerequests,employeeassetrequest,employeedetails,assets,assetdetails


app_name ="assets"


urlpatterns=[
    
    path('',HomePageView,name='home'),
    path('forms/',views.departments,name='forms'),
    path('update/department/<int:id>/',views.update_department,name='update_department'),
    path('departments/',views.departments,name='departments'), 
    path('addasset',views.asset,name='assetform'),
    path('add_department/',views.add_departments,name='departmentform'),
    path('employees', employees,name='employees'),
    # path('employee_assets', views.employee_assets,name='employee_assets'),
    path('employeerequests', employeeassetrequest,name='employeerequests'),
    path('employeedetails/<int:id>', employeedetails,name='employeedetails'),
    path('dashboard',DashBoardView,name='dashboard'),
    path('assets',assets, name='assets'),
    path('updateasset/<int:id>/',views.update_asset,name='updateasset'),
    path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
    path('managerrequest/',views.managerrequest,name='managerrequest'),
    path('assetdetails/<int:id>', views.assetdetails,name='assetdetails'),
    path('delete/<int:id>/', views.delete_asset,name='delete_asset'),







 ]
 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

