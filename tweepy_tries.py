#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 21:32:56 2018

@author: mdrygajlo
"""

import tweepy
import pandas as pd

credentials = pd.read_csv("credentials.csv")
consumer_key = credentials.iloc[0,0]
consumer_secret = credentials.iloc[0,1]
access_token = credentials.iloc[0,2]
access_token_secret = credentials.iloc[0,3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
