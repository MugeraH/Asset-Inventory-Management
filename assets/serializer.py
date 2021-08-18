from rest_framework import serializers
from .models import EmployeeAssetRequest

class EmployeeAssetRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAssetRequest
        fields = '__all__'