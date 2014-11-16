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
print "Home timeline"
print "============="

print
print "La home timeline son los tweets míos y de los que sigo"
print

tweets = twitter.get_home_timeline()
for tweet in tweets:
    print "%d -> %s" % (tweet['id'], tweet['text'])

print
print "User timeline"
print "============="

print
print "La user timeline son los tweets míos"
print

tweets = twitter.get_user_timeline()
for tweet in tweets:
    print "%d -> %s" % (tweet['id'], tweet['text'])

print
print "Mentions timeline"
print "================="

print
print "La mentions timeline son los tweets donde aparezco como @arduinoandoain"
print

tweets = twitter.get_mentions_timeline()
for tweet in tweets:
    print "%d -> %s" % (tweet['id'], tweet['text'])

