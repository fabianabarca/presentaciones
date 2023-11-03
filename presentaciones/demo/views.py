from django.shortcuts import render

# Create your views here.


def demo(request):
    return render(request, "demo.html")


def programming(request):
    context = {
        "repl1": "a = 5" + 
            "\nb = 6" +
            "\nc = 7" +
            "\ns = (a + b + c) / 2" +
            "\narea = (s*(s-a)*(s-b)*(s-c)) ** 0.5" +
            "\nprint('El area del triangulo es %0.2f' %area)",
        "repl2": "import numpy as np" +
            "\n\narray = np.array([" +
            "\n\t[3, 7, 1]," +
            "\n\t[10, 3, 2]," +
            "\n\t[5, 6, 7]" +
            "\n])" +
            "\nprint(array)" +
            "\nprint()" +
            "\nprint(np.sort(array, axis=None))" +
            "\nprint(np.sort(array, axis=1))" +
            "\nprint(np.sort(array, axis=0))",
        "repl3": "from scipy import linalg" +
            "\nimport numpy as np" +
            "\n\narr = np.array([[5,4],[6,3]])" +
            "\neg_val, eg_vect = linalg.eig(arr)" +
            "\nprint(eg_val)" +
            "\nprint(eg_vect)",
        "repl4": "import matplotlib.pyplot as plt" +
            "\nimport numpy as np" +
            "\n\nx = np.random.randn(1000)" +
            "\ny = np.random.randn(1000)" +
            "\nfig, ax = plt.subplots()" +
            "\nax.scatter(x, y)" +
            "\nfig",
        "repl5": "import pandas as pd" +
            "\n\ndf = pd.DataFrame({'num_legs': [2, 4, 8, 0]," +
            "\n\t'num_wings': [2, 0, 0, 0]," +
            "\n\t'num_specimen_seen': [10, 2, 1, 8]}," +
            "\n\tindex=['falcon', 'dog', 'spider', 'fish'])" +
            "\ndf"
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
