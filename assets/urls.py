from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView
from . import views



app_name ="assets"


urlpatterns=[
    
path('',HomePageView,name='home'),
    
path('asset/',views.asset,name='assetform'),
path('department/',views.department,name='departmentform')



 ]
 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

