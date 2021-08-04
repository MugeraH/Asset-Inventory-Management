from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import Admin, Manager,Employee, User

class EmployeeSignUpForm(UserCreationForm):
    employee = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        employee.objects.add(*self.cleaned_data.get('pk=1'))
        return user


