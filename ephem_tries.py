# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import ephem
import pandas as pd

# ---------------------------------------------------------------------------
# will run loops over those values
places = ['Paris',
          'Warsaw',
          'Berlin',
          'Prague',
          'New York',
          'Sydney',
          'Sao Paulo',
          'Johannesburg',
          'Seoul',
        ]

dates = ['2017/01/15', '2017/02/15', '2017/03/15', '2017/04/15', '2017/05/15',
         '2017/06/15', '2017/07/15', '2017/08/15', '2017/09/15', '2017/10/15',
         '2017/11/15', '2017/12/15',]

# ---------------------------------------------------------------------------
# Observer example - test
observer = ephem.city('Warsaw')
date = ephem.Date('2017/05/22')
observer.date = date
sun = ephem.Sun()
x = ephem.localtime(observer.previous_rising(sun))
y = ephem.localtime(observer.next_setting(sun))

# ---------------------------------------------------------------------------
# Run the loop to collect data about rising and setting of Sun
# on a given day, in a given city.
# Keep it in DataFrame with Cities as columns and dates as index.

rises = pd.DataFrame(index=dates, columns=places)
settings = pd.DataFrame(index=dates, columns=places)
transits = pd.DataFrame(index=dates, columns=places)

for place in places:
    for date in dates:
        observer = ephem.city(place)
        ob_data = ephem.Date(date)
        observer.date = ob_data
        sun = ephem.Sun()
        rises.loc[date,place] = ephem.localtime(observer.previous_rising(sun)).time()
        settings.loc[date,place] = ephem.localtime(observer.next_setting(sun)).time()
        transits.loc[date,place] = ephem.localtime(observer.previous_transit(sun)).time()


# ---------------------------------------------------------------------------
# Bokeh

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox, column
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider
from bokeh.plotting import figure, output_file, show

# output file name
output_file("visuals.html")


# create some widgets
slider = Slider(start=1, end=12, value=1, step=1, title="Month Slider")
button_group = RadioButtonGroup(labels=["Rise", "Transition", "Set"], active=0)
# select = Select(title="Option:", value="Paris", options=places)

# scatter plot
x = places
y = rises.iloc[0,:]

p = figure(plot_width=600, plot_height=500, y_axis_type='datetime')
# p.circle(x, y, size=20, color='navy', alpha=0.5)
p.line(x,y)

show(p)
# put the results in a row
#show(column(p, widgetbox(slider, button_group, width=600)))


#plot constructions

# p = figure(x_range=places)
# p.circle(x, y, size=9, fill_color="orange", line_color="blue", line_width=2)
