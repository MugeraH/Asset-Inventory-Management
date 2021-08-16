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
from assets import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("assets.urls")),
    path('profile/', user_views.profile, name='profile'),
    path('profile_page/', user_views.profile_page, name='profile_page'),
    # path('signup/',SignupView.as_view(),name='signup'),
    path('signup/',SignupView,name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout')


]
