from django.shortcuts import get_object_or_404, render
from .models import Sesion

# Create your views here.


def index(request):
    return render(request, "index.html")


def inicio(request):
    return render(request, "home.html")


def anuncios(request):
    return render(request, "news.html")
