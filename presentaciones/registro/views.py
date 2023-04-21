from django.shortcuts import get_object_or_404, render


# Create your views here.

def registro(request):
    
    return render(request, 'registro.html')