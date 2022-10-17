from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('syllabus', views.show_syllabus, name='list-syllabus'),
]
