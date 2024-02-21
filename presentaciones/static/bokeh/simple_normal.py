from bokeh.plotting import figure, show
from bokeh.models.annotations.labels import Label
import numpy as np
from scipy.stats import norm

# prepare some data
N = norm(0, 1)
x = np.linspace(-5, 5, 100)
y = N.pdf(x)

# create a new plot with a title and axis labels
p = figure(
    title="Distribución normal estándar",
    height=300,
    sizing_mode="stretch_width",
)
p.toolbar.autohide = True

# add a line renderer with legend and line thickness
p.line(x, y, line_width=3)

# show the results
show(p)
