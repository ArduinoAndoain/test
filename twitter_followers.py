# -*- coding: utf-8 -*-

from twython import Twython

APP_KEY = 'feMtEQ9VSw6WlfGENeNZI8ujr'
APP_SECRET = 'p6OFP1jW16MqAZ9wCHRAvY98n8czn9Dn8qwTVImrTVhSoNC6il'

TOKEN = '2871354843-Dth7fMCgLxvtNxz8XKckbJ0axCehh5eKyMqybjE'
TOKEN_SECRET = '1c3Uaxttd9KrhtPJiyjgJSbzfzaysAQKvVM0P1NVUJkuu'

# Conexión a twitter
twitter = Twython(APP_KEY, APP_SECRET, TOKEN, TOKEN_SECRET)
tweets = twitter.get_home_timeline(count=1)
for tweet in tweets:
    print(tweet['text'])

print
print "My Settings"
print "==========="

settings = twitter.get_account_settings()
#print settings
print "I am @%s" % settings['screen_name']

print
print "My friends"
print "=========="

list = twitter.get_friends_list()
for friend in list['users']:
    print "I follow user @%s, name %s, id %d" % (
        friend['screen_name'], friend['name'], friend['id'])

print
print "My followers"
print "============"

list = twitter.get_followers_list()
for friend in list['users']:
    print "User @%s, name %s, id %d is following me" % (
        friend['screen_name'], friend['name'], friend['id'])
    #print friend
