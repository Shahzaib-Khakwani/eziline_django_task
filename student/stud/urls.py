from django.urls import path

from . import views

app_name = 'stud'

urlpatterns = [
    path('', views.index, name='list_student'),
    path('student-list/', views.studentList, name='list_student_json'),
    path('create/', views.CreateUpdateStudent, name='create'),
    path('update/<int:pk>/', views.CreateUpdateStudent, name='update'),
    path('delete/<int:pk>/', views.Delete, name='delete'),
]