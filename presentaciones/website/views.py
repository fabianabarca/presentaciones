from django.shortcuts import get_object_or_404, render
from .models import Sesion

# Create your views here.

def index(request):
    sesiones = Sesion.objects.all()
    context = {
        'sesiones': sesiones,
    }
    return render(request, 'index.html', context)