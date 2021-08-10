from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import  Department, Asset,EmployeeAssetRequest,ManagerRequest,EmployeeAsset




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



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    

    class Meta:
        model = User
        fields = ['username', 'email',]


class ProfileUpdateForm(forms.ModelForm):
    

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'phone' ]

        

