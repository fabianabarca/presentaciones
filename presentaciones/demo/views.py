from django.shortcuts import render
from .models import Snippet

# Create your views here.


def demo(request):
    return render(request, "demo.html")


def programming(request):
    snippet1 = Snippet.objects.get(id="snippet1")
    snippet2 = Snippet.objects.get(id="snippet2")
    snippet3 = Snippet.objects.get(id="snippet3")
    snippet4 = Snippet.objects.get(id="snippet4")
    snippet5 = Snippet.objects.get(id="snippet5")
    context = {
        "snippet1": snippet1,
        "snippet2": snippet2,
        "snippet3": snippet3,
        "snippet4": snippet4,
        "snippet5": snippet5
    }
    return render(request, "programming.html", context)


def visualizations(request):
    return render(request, "visualizations.html")


def equations(request):
    return render(request, "equations.html")


def example(request):
    return render(request, "example.html")


def interactivity(request):
    return render(request, "interactivity.html")
