import tweepy
import csv
from textblob import TextBlob

threshold = 0

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

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
