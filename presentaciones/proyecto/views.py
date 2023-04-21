from django.shortcuts import get_object_or_404, render


# Create your views here.

def proyecto(request):
    
    return render(request, 'proyecto.html')