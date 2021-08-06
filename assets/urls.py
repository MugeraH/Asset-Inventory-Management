from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView,DashBoardView
from . import views

app_name ="assets"


urlpatterns=[
    
    path('',HomePageView,name='home'),
    path('forms/',views.departments,name='forms'),
    path('update_department/<int:dept_id>/',views.update_department,name='update_department'),
    path('departments/',views.departments,name='departments'), 
    path('asset/',views.asset,name='assetform'),
    path('add_department/',views.add_departments,name='departmentform'),
    path('employee_dashboard/', views.employee_dashboard,name='employee_dashboard'),
    path('employee_assets/', views.employee_assets,name='employee_assets'),
    path('employee_requests/', views.employee_requests,name='employee_requests'),
    path('dashboard',DashBoardView,name='dashboard'),


 ]
 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

