from bokeh.plotting import figure, output_file, show
from bokeh.util.hex import axial_to_cartesian, hexbin
from bokeh.transform import linear_cmap
import numpy as np

output_file("test.html")

p = figure(plot_width=900, plot_height=400, tools="pan,reset,save")
p.circle_cross(x=[1,2,3,4,5], y=[1,4,9,16,25], size=20, alpha=0.5)

show(p)
n = 5000
q = np.random.standard_normal(n)
r = np.random.standard_normal(n)

bins = hexbin(q,r,0.1)

s = figure(tools='wheel_zoom,reset', match_aspect=True, plot_width=600, plot_height=600, background_fill_color='#440154')
s.grid.visible = True

s.hex_tile(q='q',r='r', size=0.1, line_color=None, source=bins,
           fill_color=linear_cmap('counts','Viridis256',0,max(bins.counts)))


show(s)