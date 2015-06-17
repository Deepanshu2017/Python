__author__ = 'deepanshu'

from twitter import *

# Enter your twitter credentials here in between quotes
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = ''


def compose_tweet(tweet):
    # print 'I am here'    #Debug
    t = Twitter(auth=OAuth(access_key, access_secret, consumer_key, consumer_secret))
    try:
        t.statuses.update(status=tweet)
    finally:
        "Error in Authentication"
