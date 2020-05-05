import requests
import pandas as pd
import tweepy as tw
import  collections as cl

consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

auth = tw.OAuthHandler(consumer_key, consumer_secret)
print("This is Auth: ",auth)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "#Python"
date_since = "2019-11-01"


# Collect tweets
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(10)
print(tweets)

# most_words = []
for tweet in tweets:
     print(tweet.text)
    
