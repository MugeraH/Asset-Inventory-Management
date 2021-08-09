from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import HomePageView


app_name ="users"


urlpatterns=[
path('',HomePageView,name='home'),

]