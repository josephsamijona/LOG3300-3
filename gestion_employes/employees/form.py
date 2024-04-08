from django import forms
from employees.models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_id', 'department_name', 'location']
