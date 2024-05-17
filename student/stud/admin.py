from django.contrib import admin

from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['roll_no', 'first_name', 'last_name', 'father_name']