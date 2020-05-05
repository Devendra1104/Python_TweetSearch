import tweepy as tw

consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 
def fetch_tweets(username):
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    print(auth)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth)
    print(api)

    number_of_tweets=10
    tweets = api.user_timeline(screen_name=username)

    # tmp = []
    for tweet in tweets:
        print(tweet.text)

fetch_tweets('@Arsenal')
