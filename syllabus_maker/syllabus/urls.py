from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('syllabus', views.show_syllabus, name='list-syllabus'),
    
]
