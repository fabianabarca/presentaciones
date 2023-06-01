from django.shortcuts import get_object_or_404, render
from .models import Sesion

# Create your views here.


def index(request):
    sesiones = Sesion.objects.all()
    context = {
        "sesiones": sesiones,
    }
    return render(request, "index.html", context)


def demo(request):
    return render(request, "demo.html")


def inicio(request):
    return render(request, "home.html")


def anuncios(request):
    return render(request, "news.html")
