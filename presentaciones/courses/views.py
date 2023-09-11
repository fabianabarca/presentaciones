from django.shortcuts import render
from .models import Course

# Create your views here.


def courses(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, "courses.html", context)


def course(request, id):
    id = id.upper()
    course = Course.objects.get(id=id)
    context = {
        "course": course
    }
    return render(request, "course.html", context)
