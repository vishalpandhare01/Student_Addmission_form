from django.contrib import admin

# Register your models here.
from .models import Course


class CourseDesplay(admin.ModelAdmin):
    list_display = ('course_title','course_disc')

admin.site.register(Course,CourseDesplay)