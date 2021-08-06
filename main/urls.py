
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView
    
    )
from users.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("assets.urls")),
    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page = '/'),name='logout')


]
