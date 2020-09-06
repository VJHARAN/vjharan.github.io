from django.contrib import admin
from courses.models import Subjects,Lesson,Class
# Register your models here.

admin.site.register(Subjects)
admin.site.register(Lesson)
admin.site.register(Class)
