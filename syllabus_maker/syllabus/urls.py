from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_syllabus, name='list-syllabus'),
    path('add_syllabus', views.add_syllabus, name='add-syllabus'),
    path('show_syllabus/<syllabus_id>', views.show_syllabus, name='show-syllabus'),
]
