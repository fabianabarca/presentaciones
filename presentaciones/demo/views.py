from django.shortcuts import render

# Create your views here.


def demo(request):
    return render(request, "demo.html")


def project(request):
    return render(request, "project.html")


def programming(request):
    return render(request, "programming.html")


def visualizations(request):
    return render(request, "visualizations.html")


def equations(request):
    return render(request, "equations.html")


def example(request):
    return render(request, "example.html")


def interactivity(request):
    return render(request, "interactivity.html")
