from django.contrib import admin
from .models import Asset,Department,EmployeeAssetRequest,ManagerRequest

# Register your models here.
admin.site.register(ManagerRequest)
admin.site.register(EmployeeAssetRequest)
admin.site.register(Asset)
admin.site.register(Department)