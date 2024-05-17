from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Student
from .forms import StudentForm

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request, 'stud/list.html', {'students':students})


def studentList(request):
    students = Student.objects.all().values()
    return JsonResponse({'students':list(students)})


@login_required
def CreateUpdateStudent(request, pk=None):
    if request.method == 'POST':
        if pk:
            student = get_object_or_404(Student, pk = pk)
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                studnet = form.save()
                return HttpResponse("Student Updated")
            else:
                return HttpResponse(form.errors)
        else:
            form = StudentForm(request.POST)
            if form.is_valid():
                student  = form.save()
                return HttpResponse("Student created")
            else:
                return HttpResponse(form.errors)
    else:
        student = None
        if pk:
            student = get_object_or_404(Student, pk=pk)
            form = StudentForm(instance=student)
            section = 'update'
        else:
            form = StudentForm()
        return render(request,"stud/createUpdate.html", {'form':form, 'student':student})


@login_required
def Delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect(reverse('stud:list_student'))