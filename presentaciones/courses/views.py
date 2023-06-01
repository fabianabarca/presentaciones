from django.shortcuts import render

# Create your views here.


def courses(request):
    return render(request, "courses.html")


def course(request):
    context = {}
    return render(request, "course.html", context)
