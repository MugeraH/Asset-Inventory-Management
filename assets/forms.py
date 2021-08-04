from django import forms
from .models import Category, Department, Asset,EmployeeAssetRequest,ManagerRequest

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields= ('name',)

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


class ManagerRequest(forms.ModelForm):
    class Meta:
        model=ManagerRequest
        fields= '__all__'
