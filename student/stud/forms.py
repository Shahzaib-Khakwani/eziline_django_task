from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'first_name', 'last_name', 'father_name']