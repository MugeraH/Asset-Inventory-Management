from django import forms
from .models import  Department, Asset,EmployeeAssetRequest,ManagerRequest



class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields= ('name',)


class AssetForm(forms.ModelForm):
    class Meta:
        model=Asset
        fields= '__all__'
        exclude= ('is_assigned','created_at','modified_at',)


class EmployeeAssetRequestForm(forms.ModelForm):
    class Meta:
        model=EmployeeAssetRequest
        fields= ('type','request_detail',)

class ManagerRequestForm(forms.ModelForm):
    class Meta:
        model=ManagerRequest
        fields= ('request','specs',)
        