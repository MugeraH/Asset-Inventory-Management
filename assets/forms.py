from django import forms
from .models import  Department, Asset,EmployeeAssetRequest,ManagerRequest,EmployeeAsset

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields= ('name',)

class AssetForm(forms.ModelForm):
    class Meta:
        model=Asset
        fields= ('name','description','image','category',)


class EmployeeAssetRequestForm(forms.ModelForm):
    class Meta:
        model=EmployeeAssetRequest
        fields= ('type','request_detail','quantity')

class ManagerRequestForm(forms.ModelForm):
    class Meta:
        model=ManagerRequest
        fields= ('request','specs','quantity')


class DepartmentAssigningForm(forms.ModelForm):
    class Meta:
        model=Department
        fields= ('manager',)

class AssetAssigningForm(forms.ModelForm):
    class Meta:
        model=Asset
        fields= ('department',)

class EmployeeAssetForm(forms.ModelForm):
    class Meta:
        model=EmployeeAsset
        fields= ('employee',)


        

