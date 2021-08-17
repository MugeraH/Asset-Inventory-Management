from rest_framework import serializers
from django import forms
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ('name', 'description', 'category')
