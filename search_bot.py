import tweepy
import time
import os
from os import environ

#You will need to get these from twitter and keep them SECRET! Apply for a developer account and follow the instructions.
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
key = environ['ACCESS_KEY']
secret = environ['ACCESS_SECRET']

#The tweepy documentation is a must read and you will find the code below there.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#Input hashtag you are targeting.
hashtag = "pennystocks"

#Input amount of tweets you want tyo engage with. Keep it reasonable to stay within rate limits.
tweetnumber = 200

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)


def search_bot():
	"""Function to engage user's twitterbot with other twitter users. The tweepy documentation shows you different ways to engage."""
	for tweet in tweets:
		try:
			tweet.retweet()
			api.create_favorite(tweet.id)
			time.sleep(400)
			
		except tweepy.TweepError as e:
			print(e.reason)
			
#Call function. Rinse. Repeat. Enjoy.
search_bot()
