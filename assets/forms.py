from django import forms
from .models import  Department, Asset,EmployeeAssetRequest,ManagerRequest
from django.contrib.auth.models import User
from .models import Profile




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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    

    class Meta:
        model = User
        fields = ['username', 'email',]


class ProfileUpdateForm(forms.ModelForm):
    

    class Meta:
        model = Profile
        fields = ['image', 'bio', 'phone' ]
