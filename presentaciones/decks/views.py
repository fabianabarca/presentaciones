from django.shortcuts import get_object_or_404, render

# Create your views here.

def lista(request):
    return render(request, 'lista.html')

def clase(request, numero):
    presentacion = 'clases/' + str(numero) + '.html'
    context = {
        'presentacion': presentacion,
        'numero': numero
    }
    return render(request, 'clase.html', context)