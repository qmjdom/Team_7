from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('syllabus', views.show_syllabus, name='list-syllabus'),
    
]
