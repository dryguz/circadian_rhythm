#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:32:56 2018

@author: mdrygajlo
"""

import tweepy
import pandas as pd

credentials = pd.read_csv("credentials.csv")
customer_key = credentials.iloc[0,0]
customer_secret = credentials.iloc[0,1]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

