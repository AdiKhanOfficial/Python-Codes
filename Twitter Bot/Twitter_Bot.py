import tweepy

api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""
# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_user_tweets(user, limit=10):
    user_tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)
    return user_tweets


def post_tweet(message):
    my_tweet = api.update_status(status=message)
    return my_tweet


user = 'CoinMarketCap'

user_tweets = get_user_tweets(user, 1)

for tweet in user_tweets:
    print(tweet.full_text + "\n\n")
    print(post_tweet(tweet.full_text))
