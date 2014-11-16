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

# problem: I just got a TwythonRateLimitError: Twitter API returned a 429 (Too Many Requests), Rate limit exceeded

"""
{
    u'contributors': None,
    u'truncated': False,
    u'text': u'@ArduinoAndoain Hello Arduino, give the #time',
    u'in_reply_to_status_id': None,
    u'id': 534102912994009088L,
    u'favorite_count': 0,
    u'source': u'<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>',
    u'retweeted': False,
    u'coordinates': None,
    u'entities': {
        u'symbols': [],
        u'user_mentions': [{
                u'id': 2871354843L,
                u'indices': [0, 15],
                u'id_str': u'2871354843',
                u'screen_name': u'ArduinoAndoain',
                u'name': u'Arduino Andoain'
            }],
        u'hashtags': [{
                u'indices': [40, 45],
                u'text': u'time'
            }],
        u'urls': []
        },
    u'in_reply_to_screen_name': u'ArduinoAndoain',
    u'id_str': u'534102912994009088',
    u'retweet_count': 0,
    u'in_reply_to_user_id': 2871354843L,
    u'favorited': False,
    u'user': {
        u'follow_request_sent': False,
        u'profile_use_background_image': True,
        u'profile_text_color': u'333333',
        u'default_profile_image': True,
        u'id': 2902026636L,
        u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png',
        u'verified': False,
        u'profile_location': None,
        u'profile_image_url_https': u'https://abs.twimg.com/sticky/default_profile_images/default_profile_5_normal.png',
        u'profile_sidebar_fill_color': u'DDEEF6',
        u'entities': {
            u'description': {
                u'urls': []
                }
            },
        u'followers_count': 0,
        u'profile_sidebar_border_color': u'C0DEED',
        u'id_str': u'2902026636',
        u'profile_background_color': u'C0DEED',
        u'listed_count': 0,
        u'is_translation_enabled': False,
        u'utc_offset': None,
        u'statuses_count': 1,
        u'description': u'',
        u'friends_count': 2,
        u'location': u'',
        u'profile_link_color': u'0084B4',
        u'profile_image_url': u'http://abs.twimg.com/sticky/default_profile_images/default_profile_5_normal.png',
        u'following': False,
        u'geo_enabled': False,
        u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png',
        u'name': u'Olivier Georg',
        u'lang': u'en',
        u'profile_background_tile': False,
        u'favourites_count': 0,
        u'screen_name': u'olivier_georg',
        u'notifications': False,
        u'url': None,
        u'created_at': u'Sun Nov 16 21:18:51 +0000 2014',
        u'contributors_enabled': False,
        u'time_zone': None,
        u'protected': False,
        u'default_profile': True,
        u'is_translator': False
        },
    u'geo': None,
    u'in_reply_to_user_id_str': u'2871354843',
    u'lang': u'en',
    u'created_at': u'Sun Nov 16 21:57:12 +0000 2014',
    u'in_reply_to_status_id_str': None,
    u'place': None
}
"""

# El hashtag: tweet['entities']['hashtags']['text'] == 'time'
# El usuario que ha mandado: tweet['user']['id']