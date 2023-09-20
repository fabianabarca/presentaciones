from django.shortcuts import render


# Create your views here.


def students(request):
    return render(request, "students.html")


# Perfil de cada usuario
def profile(request):
    return render(request, "profile.html")
