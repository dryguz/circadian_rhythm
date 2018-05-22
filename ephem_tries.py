# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import ephem
import pandas as pd

# ---------------------------------------------------------------------------
# will run loops over those values
places = {'Paris',
          'Warsaw',
          'Berlin',
          'Prague',
          'New York',
          'Sydney',
          'Sao Paulo',
          'Johannesburg',
          'Seoul',
        }

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

data = pd.DataFrame(index=dates, columns=places)

for place in places:
    for date in dates:
        observer = ephem.city(place)
        ob_data = ephem.Date(date)
        observer.date = ob_data
        sun = ephem.Sun()
        x = ephem.localtime(observer.previous_rising(sun)).time()
        y = ephem.localtime(observer.next_setting(sun)).time()
        data.loc[date,place]=(x,y)
        
# ---------------------------------------------------------------------------
# Twitter part

    

    