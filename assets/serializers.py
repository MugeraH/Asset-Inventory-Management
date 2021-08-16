from rest_framework import serializers
from django import forms
from .models import Email


# from .models import
class EmailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Email
		fields ='__all__'