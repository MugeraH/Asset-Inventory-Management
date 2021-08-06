from adminManagerEmployee import views as user_views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("assets.urls")),
    path('adminManagerEmployee', include('adminManagerEmployee.urls'), name='adminManagerEmployee'),
]
