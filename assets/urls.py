from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import HomePageView,DashBoardView,employees,employeerequests,employeeassetrequest,employeedetails,assets,assetdetails,addasset
addasset


app_name ="assets"


urlpatterns=[
    
    
 
    path('update/department/<int:id>/',views.update_department,name='update_department'),
    path('departments/',views.departments,name='departments'), 
    path('addasset',views.addasset,name='assetform'),
    
    path('employeedetails/<int:id>', employeedetails,name='employeedetails'),
    path('delete_employee/<int:id>', views.delete_employee,name='delete_employee'),
    path('employeeassetrequest',views.employeeassetrequest,name='employeeassetrequest'),
    path('managerrequest/',views.managerrequest,name='managerrequest'),
    path('assetdetails/<int:id>', views.assetdetails,name='assetdetails'),
    path('delete/<int:id>/', views.delete_asset,name='delete_asset'),
    
    path('dashboard',DashBoardView,name='dashboard'),
    
    path('employees',views.employees,name='employees'),
    path('dept_employees',views.dept_employees,name='dept_employees'),
    path('dashboard',DashBoardView,name='dashboard'),
    path('manager_dashboard',views.managerDashBoardView,name='manager_dashboard'),
    path('employee_dashboard',views.employeeDashBoardView,name='employee_dashboard'),
    # path('employeedetails/<int:id>', views.employeedetails,name='employeedetails'),
    path('department_detail/<int:id>',views.department_detail,name='department_detail'),
 
    path('dept_assets/',views.dept_assets,name='dept_assets'),
    path('employee_assets/',views.employee_assets,name='employee_assets'),
  
    path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
    path('assign_asset/<int:id>',views.assign_asset,name='assign_asset'),
    path('assign_asset_user/<int:id>',views.assign_asset_user,name='assign_asset_user'),
    path('unassign_asset_user/<int:id>',views.unassign_asset_user,name='unassign_asset_user'),
    path('unassign_asset_dept/<int:id>',views.unassign_asset_dept,name='unassign_asset_dept'),
    # path('employeedetails/<int:id>', views.employeedetails,name='employeedetails'),
    path('department_detail/<int:id>',views.department_detail,name='department_detail'),
    path('delete_department/<int:id>',views.delete_department,name='delete_department'),
    path('assets/',views.assets,name='assets'),
    path('update_asset/<int:id>/',views.update_asset,name='update_asset'),
    path('employeeassetrequest/',views.employeeassetrequest,name='employeeassetrequest'),
    
    path('assign_asset/<int:id>',views.assign_asset,name='assign_asset'),
    
    path('',views.request_demo,name='request_demo'),
    
    path('assign_asset/<int:id>',views.assign_asset,name='assign_asset'),
    path('dept_requests',views.dept_requests,name='dept_requests'),
    path('employee_requests',views.employee_requests,name='employee_requests'),
    path('employeerequestdetails/<int:id>', views.employeerequestdetails,name='employeerequestdetails'),
    path('managerrequestdetails/<int:id>', views.managerrequestdetails ,name='managerrequestdetails'),
    path('update_manager_request/<int:id>', views.update_manager_request ,name='update_manager_request'),
    path('update_employee_request/<int:id>', views.update_employee_request ,name='update_employee_request'),
    path('delete_employee_request/<int:id>', views.delete_employee_request ,name='delete_employee_request'),
    path('delete_manager_request/<int:id>', views.delete_manager_request ,name='delete_manager_request'),
    path('requests', views.requests,name='requests'),
    path('add_departments/',views.add_departments,name='add_departments'),
    path('employee_assets',views.employee_assets,name='employee_assets'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

