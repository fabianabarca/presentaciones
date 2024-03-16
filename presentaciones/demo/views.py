from django.shortcuts import render

# Create your views here.


def demo(request):
    return render(request, "demo.html")


def project(request):
    if request.user.is_staff:
        role = "presenter"
    else:
        role = "viewer"
    context = {"role": role}
    return render(request, "project.html", context)



def programming(request):

    context = {
        "example1": 
"""from pyscript import display

display("¡Hola Mundo!")""",

        "example2": 
"""import numpy as np
import pandas as pd
from pyscript import display

df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD')).cumsum()
display(df)"""
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
