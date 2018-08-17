# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import ephem
import pandas as pd
import numpy as np



# ---------------------------------------------------------------------------
# will run loops over those values
places = ['Paris',
          'Berlin',
          'Prague',
          'Warsaw',
        ]
# places = list(cities._city_data.keys())

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

rises = pd.DataFrame(index=places, columns=dates)
settings = pd.DataFrame(index=places, columns=dates)
transits = pd.DataFrame(index=places, columns=dates)



for place in places:
    for date in dates:
        observer = ephem.city(place)
        ob_data = ephem.Date(date)
        observer.date = ob_data
        sun = ephem.Sun()

        a = ephem.localtime(observer.previous_rising(sun)).time()
        b = ephem.localtime(observer.previous_transit(sun)).time()
        c = ephem.localtime(observer.next_setting(sun)).time()

        rises.loc[place,date] = a
        transits.loc[place,date] = b
        settings.loc[place,date] = c


# ---------------------------------------------------------------------------
# Bokeh

from bokeh.layouts import widgetbox, column
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider
from bokeh.plotting import figure, output_file, show


# output file name
output_file("visuals.html")


# data for plot - classic
x = places
y1 = rises.iloc[:,0]
y2 = transits.iloc[:,0]
y3 = settings.iloc[:,0]

# create some widgets

button_group = RadioButtonGroup(labels=["Rise", "Transition", "Set"], active=0)
# select = Select(title="Option:", value="Paris", options=places)

# with ColumnDataSource
rises['display'] = pd.Series(rises.loc[:,'2017/01/15'], index=rises.index)
transits['display'] = pd.Series(transits.loc[:,'2017/01/15'], index=transits.index)
settings['display'] = pd.Series(settings.loc[:,'2017/01/15'], index=settings.index)

source1 = ColumnDataSource(rises)
source2 = ColumnDataSource(transits)
source3 = ColumnDataSource(settings)

q = figure(plot_width=600, plot_height=500, x_range=places, y_axis_type='datetime')

q.circle(x='index', y='display', size=15, color='navy', legend='Rise', source=source1)
q.line(x='index', y='display', line_width=2, legend="Rise", source=source1)

q.square(x='index', y='display', size=15, color='orangered', legend='Transit', source=source2)
q.line(x='index', y='display', line_width=2, color='orangered', legend='Transit', source=source2)

q.circle(x='index', y='display', size=15, color='peru', legend='Setting', source=source3)
q.line(x='index', y='display', line_width=2, color='peru', legend='Setting', source=source3)

q.legend.location = "bottom_left"

callback = CustomJS(args=dict(source1=source1, source2=source2, source3=source3), code=
                    """
                    var data1 = source1.data
                    var data2 = source2.data
                    var data3 = source3.data
                    var f = cb_obj.value
                    var x = data1['index']
                    var y1 = data1['display']
                    var y2 = data2['display']
                    var y3 = data3['display']
                    if (f < 10 ) {
                    date = '2017/0' + f + '/15'
                    } else {
                    date = '2017/' + f + '/15'
                    }
                    change1 = data1[date]
                    change2 = data2[date]
                    change3 = data3[date]
                    for(var i = 0; i < x.length; i++) {
                     y1[i] = change1[i]
                     y2[i] = change2[i]
                     y3[i] = change3[i]
                    }
                    source1.change.emit()
                    source2.change.emit()
                    source3.change.emit()
                    """
                    )
slider = Slider(start=1, end=12, value=1, step=1, title="Month Slider")
slider.js_on_change('value', callback)
show(column(q, widgetbox(slider, button_group, width=600)))
