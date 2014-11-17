# -*- coding: utf-8 -*-

from twython import Twython
from time import gmtime, strftime
import datetime
import os

APP_KEY = 'feMtEQ9VSw6WlfGENeNZI8ujr'
APP_SECRET = 'p6OFP1jW16MqAZ9wCHRAvY98n8czn9Dn8qwTVImrTVhSoNC6il'

TOKEN = '2871354843-Dth7fMCgLxvtNxz8XKckbJ0axCehh5eKyMqybjE'
TOKEN_SECRET = '1c3Uaxttd9KrhtPJiyjgJSbzfzaysAQKvVM0P1NVUJkuu'

# Conexión a twitter
twitter = Twython(APP_KEY, APP_SECRET, TOKEN, TOKEN_SECRET)

# 1 - Guardar a un fichero la lista de ids de tweets

print """
Mentions timeline"
=================

La mentions timeline son los tweets donde aparezco como @arduinoandoain
"""

def save_mentions_timeline_id(file):
    # get timeline
    tweets = twitter.get_mentions_timeline()

    file.write("[\n1L,\n")

    for tweet in tweets:
        file.write(str(tweet['id']))
        file.write("L,\n")

    file.write("]")

def save_mentions_timeline(filename):
    tweets = twitter.get_mentions_timeline(since_id=1L)
    for tweet in tweets:
        print(tweet)

def mentions_timeline_since(tweet_id):
    print "need tweets since ", tweet_id, type(tweet_id)
    tweets = twitter.get_mentions_timeline(since_id=tweet_id)
    print len(tweets)
    return tweets

# problem: I just got a TwythonRateLimitError: Twitter API returned a 429 (Too Many Requests), Rate limit exceeded

# with open("outputs/mentions_timeline_ids.txt", "w") as f: save_mentions_timeline_id(f)

# Vamos a crear un tweet para un usuario que ha pedido la hora

def get_hashtags(tweet):
    """
    Devuelve la lista de hashtags sin #
    """
    hashtags = tweet['entities']['hashtags']
    hashtags = [h['text'] for h in hashtags]
    return hashtags

def respond_to_tweets_since(last_id):
    """
    Contesta a todos los tweets pidiendo la hora
    devuelve el id del último tweet procesado
    """
    tweet_id = last_id
    for tweet in reversed(mentions_timeline_since(last_id)):
        # id del tweet
        tweet_id = tweet['id']
        requesting_user = tweet['user']['screen_name']
        if 'time' in get_hashtags(tweet):
            hora = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S.%f")
            # hora = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
            response = "Hi @%s, #time is %s" % (requesting_user, hora)
            print "respond to tweet %d is '%s'" % (tweet_id, response)
            twitter.update_status(status=response, in_reply_to_status_id=tweet_id)
    else:
        print "No new tweet to answer"

    # devolvemos el id del último tweet procesado
    return tweet_id


def read_last_tweet_id(fname):
    last_id = 1L
    if os.path.isfile(fname):
        with open(fname, "r") as f:
            last_id = long(f.read())
    return last_id

def write_last_tweet_id(last_id, fname):
    with open(fname, "w") as f:
        f.write(str(last_id))

LAST_ID_FILE = "last_id.txt"
def process_iteration():
    last_id = read_last_tweet_id(LAST_ID_FILE)
    print "last_id is %s" % last_id
    last_id = respond_to_tweets_since(last_id)
    write_last_tweet_id(last_id, LAST_ID_FILE)

process_iteration()

# send a tweet to @olivier_georg
# twitter.update_status(status="Hello @olivier_georg from ArduinoAndoain! :D")