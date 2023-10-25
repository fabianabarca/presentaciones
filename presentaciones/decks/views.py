from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

def decks(request):
    return render(request, 'decks.html')

def deck(request, slug):
    presentacion = 'clases/' + str(slug) + '.html'
    context = {
        'presentacion': presentacion,
    }
    return render(request, 'deck.html', context)

