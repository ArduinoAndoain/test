# -*- coding: utf-8 -*-

from twython import Twython

APP_KEY = 'feMtEQ9VSw6WlfGENeNZI8ujr'
APP_SECRET = 'p6OFP1jW16MqAZ9wCHRAvY98n8czn9Dn8qwTVImrTVhSoNC6il'

TOKEN = '2871354843-Dth7fMCgLxvtNxz8XKckbJ0axCehh5eKyMqybjE'
TOKEN_SECRET = '1c3Uaxttd9KrhtPJiyjgJSbzfzaysAQKvVM0P1NVUJkuu'

# Conexión a twitter
twitter = Twython(APP_KEY, APP_SECRET, TOKEN, TOKEN_SECRET)

# 1 - Guardar a un fichero la lista de ids de tweets

print
print "Mentions timeline"
print "================="

print
print "La mentions timeline son los tweets donde aparezco como @arduinoandoain"
print

tweets = twitter.get_mentions_timeline()
for tweet in tweets:
    print(tweet['id'], tweet['text'])
idlist = "[1L, " + "L, ".join([str(t['id']) for t in tweets]) + "L]"
print idlist

tweets = twitter.get_mentions_timeline(since_id=1L)
for tweet in tweets:
    print(tweet)
