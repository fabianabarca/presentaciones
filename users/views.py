from django.shortcuts import render, redirect
from .models import Student


# Create your views here.


def students(request):
    if request.user.is_staff:
        students = Student.objects.all()
        context = {"students": students}
        return render(request, "students.html", context)
    else:
        return redirect("home")


# Perfil de cada usuario
def profile(request):
    student = Student.objects.get(user=request.user)
    context = {"student": student}
    return render(request, "profile.html", context)
