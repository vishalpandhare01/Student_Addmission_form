from django.shortcuts import render
from django.urls import path
from courses.models import Course

def index(request):
    course=Course.objects.all()
    if request.method == "GET":
        st=request.GET.get("course")
        if st!=None:
            course=Course.objects.filter(course_title__icontains=st)
    data={
        "course":course,
    }
    return render(request,"index.html",data)