from django.contrib import admin
from .models import Instructor
from .models import Course
from .models import Signature

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Signature)

