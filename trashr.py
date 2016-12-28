#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, config
import signal
import random

# Import keys from config file
#TODO add a way to override this config file from the CLI
CONSUMER_KEY = config.consumerkey
CONSUMER_SECRET = config.consumersecret
ACCESS_KEY = config.accesskey
ACCESS_SECRET = config.accesssecret

# Get auth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

responses = ["Thanks for the reminder!",
             "You're the bestest in the westest!",
             "One of these days I won't need you to tell me...",
             "What would I do without you?!"]

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        screen_name = status.user.screen_name text = status.text
        # Choose from one of the random responses
        randomstring = random.choice(responses)
        updatestatus = "@" + screen_name + " " + randomstring
        print(updatestatus)
        api.update_status(status=updatestatus)

    def on_error(self, status_code):
        if status_code == 420:
            return False

#TODO: make this nohup itself so you don't have to launch via
# `nohup python blah.py`
if __name__ == "__main__":
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['Hey @mscman, remember to take the trash to the curb tonight'])
