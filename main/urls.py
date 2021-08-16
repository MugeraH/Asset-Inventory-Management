from django.contrib import admin
from django.db.models import manager
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

from django.urls import path, include
from django.contrib.auth.models import User
from assets.models import EmployeeAsset
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class EmployeeAssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeAsset
        fields = ['employee', 'asset',]

# ViewSets define the view behavior.
class EmployeeAssetViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAsset.objects.all()
    serializer_class = EmployeeAssetSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'employeeasset', EmployeeAssetViewSet)


urlpatterns = [
    path('api-employeeasset/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('',include("assets.urls")),
    path('profile/', user_views.profile, name='profile'),
    path('profile_page/', user_views.profile_page, name='profile_page'),
    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout')


]