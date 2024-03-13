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
from scipy import stats
from matplotlib import pyplot as plt
from pyscript import display

rv = stats.norm(0, 1)
rv_samples = rv.rvs(size=1000)
fig, ax = plt.hist(rv_samples, bins=30, density=True)
# x = np.linspace(-4, 4, 100)
# plt.plot(x, rv.pdf(x))

display("fig")"""
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
