import tweepy
import csv
from textblob import TextBlob

threshold = 0

consumer_key = "M3IyWsVP1XGJjeab0NKUxeKSh"
consumer_secret = "iIkXKKJGWoRHnG0wKhB8nI07Ew56FghQpY2aPHXP01g8nBPLR8"

access_token = "869979232327393280-eZIHi2HOy1FBTA3x2smgIXekdzxS9Dg"
access_token_secret = "76htlTCQjZMTgStVHwQVSbK6TcIJY03onGvlnqEqYHiPS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

with open('tweet.csv', 'w') as w:
    writer = csv.writer(w)

    for tweet in public_tweets:
        txt = str(tweet.text)
        writer.writerow(txt)
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        if(analysis.sentiment[0] < threshold):
            print('Negative')
        else:
            print('Positive')

w.close()
