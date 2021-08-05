from django.contrib import admin
from .models import Asset,Department,EmployeeAssetRequest,ManagerRequest,Profile,EmployeeAsset

# Register your models here.
admin.site.register(ManagerRequest)
admin.site.register(EmployeeAssetRequest)
admin.site.register(Asset)
admin.site.register(Department)
admin.site.register(Profile)
admin.site.register(EmployeeAsset)
