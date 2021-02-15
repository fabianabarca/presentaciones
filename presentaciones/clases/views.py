from django.shortcuts import get_object_or_404, render

# Create your views here.

def clase(request):
    return render(request, 'clase.html')