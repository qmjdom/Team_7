from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Course
from .forms import CourseForm

def add_syllabus(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_syllabus?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'add_syllabus.html', {'form':form, 'submitted':submitted})

def list_syllabus(request):
    details_list = Course.objects.all()
    return render(request, 'syllabus.html', 
    {'details_list' : details_list})

def show_syllabus(request, syllabus_id):
    syllabus = Course.objects.get(pk=syllabus_id)
    return render(request, 'show_syllabus.html', 
    {'syllabus' : syllabus})

def home_page(request):
    return render(request, 'homepage.html')
