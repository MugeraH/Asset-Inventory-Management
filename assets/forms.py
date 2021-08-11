from django import forms
from .models import  Department, Asset,EmployeeAssetRequest,ManagerRequest,EmployeeAsset,Profile,User




class EmployeeProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields= ('department','role')
        

        
        
class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields= ('name','description')

class AssetForm(forms.ModelForm):
    class Meta:
        model=Asset
        fields= ('name','description','image','category',)
     

class EmployeeAssetRequestForm(forms.ModelForm):
    class Meta:
        model=EmployeeAssetRequest
        fields= ('type','request_detail','quantity','urgency')

class ManagerRequestForm(forms.ModelForm):
    class Meta:
        model=ManagerRequest
        fields= ('request','specs','quantity','urgency')


class DepartmentAssigningForm(forms.ModelForm):
    class Meta:
        model=Department
        fields= ('manager',)

class AssetAssigningForm(forms.ModelForm):
    class Meta:
        model=Asset
        fields= ('department',)




        

