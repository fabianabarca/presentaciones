from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# create a new plot with a title and axis labels
p = figure(
    title="Ejemplo de una gráfica simple de Bokeh",
    x_axis_label="Valor de x",
    y_axis_label="Valor de y",
    height=400,
    sizing_mode="stretch_width",
)

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=2)

# show the results
show(p)
