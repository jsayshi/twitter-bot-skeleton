import tweepy
import time

consumer_key = 
consumer_secret = 
key = 
secret = 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


hashtag = 
tweetnumber = 

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)



def search_bot():
	for tweet in tweets:
		try:
			api.create_favorite(tweet.id)
			
			
		except tweepy.TweepError as e:
			print(e.reason)
			
		

search_bot()