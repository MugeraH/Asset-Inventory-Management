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


class EmployeeAssetRequestForm(forms.ModelForm):
    class Meta:
        model=EmployeeAssetRequest
        fields= '__all__'
        exclude= ('user',)

class ManagerRequestForm(forms.ModelForm):
    class Meta:
        model=ManagerRequest
        fields= '__all__'
        exclude= ('user',)