from js import Bokeh

import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure

x = np.linspace(0, 4 * np.pi, 100)
y = np.sin(x)

TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

p = figure(title="Legend Example", tools=TOOLS)

p.scatter(x, y, legend_label="sin(x)")
p.scatter(x, 2 * y, legend_label="2*sin(x)", color="orange")
p.scatter(x, 3 * y, legend_label="3*sin(x)", color="green")

p.legend.title = "Markers"

Bokeh.embed.embed_item(p, "myplot")
