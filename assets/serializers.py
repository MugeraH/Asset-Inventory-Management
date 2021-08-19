from django.db.models import fields
from rest_framework import serializers
from django import forms
from .models import Asset,Department,EmployeeAssetRequest,ManagerRequest



class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name','description','created_at','modified_at','manager')
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('name', 'description', 'category')
class EmployeeAssetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAssetRequest
        fields= ('employee','type','request_detail','quantity','status','posted_date','urgency','completed')

class ManagerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerRequest
        fields= ('request','specs','quantity','posted_date','status','employee','urgency','completed')
