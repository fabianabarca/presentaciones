from django.shortcuts import render
from .models import Student


# Create your views here.


def students(request):
    return render(request, "students.html")


# Perfil de cada usuario
def profile(request):
    student = Student.objects.get(user=request.user)
    context = {
        "student": student
    }
    return render(request, "profile.html", context)
