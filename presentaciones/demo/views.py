from django.shortcuts import get_object_or_404, render


# Create your views here.

def demo(request):
    
    return render(request, 'demo.html')