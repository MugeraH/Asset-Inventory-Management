from django.db.models import fields
from rest_framework import serializers
from django import forms

from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name','description','created_at','modified_at','manager')
