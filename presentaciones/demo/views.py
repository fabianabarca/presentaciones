from django.shortcuts import render

# Create your views here.


def demo(request):
    return render(request, "demo.html")


def programming(request):
    context = {
        "variable1": """
        a = 5
        b = 6
        c = 7
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

        print('El área del triángulo es %0.2f.' %area)
        print()
        """,
        "variable2": """
        import numpy as np

        array = np.array([
            [3, 7, 1],
            [10, 3, 2],
            [5, 6, 7]
        ])

        print(array)
        print()
        print(np.sort(array, axis=None))
        print(np.sort(array, axis=1))
        print(np.sort(array, axis=0))
        """,
        "variable3": """
        from scipy import linalg
        import numpy as np

        arr = np.array([[5,4],[6,3]])
        eg_val, eg_vect = linalg.eig(arr)
        print(eg_val)
        print(eg_vect)
        print()
        """,
        "variable4": """
        import matplotlib.pyplot as plt
        import numpy as np

        x = np.random.randn(1000)
        y = np.random.randn(1000)
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        fig
        """,
        "variable5": """
        import pandas as pd

        df = pd.DataFrame({
            'num_legs': [2, 4, 8, 0],
            'num_wings': [2, 0, 0, 0],
            'num_specimen_seen': [10, 2, 1, 8]},
            index=['falcon', 'dog', 'spider', 'fish'])
        df
        """
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
