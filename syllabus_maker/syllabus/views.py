from django.shortcuts import render
from .models import Course

def show_syllabus(request):
    details_list = Course.objects.all()
    return render(request, 'syllabus.html', 
    {'details_list' : details_list})
