import tweepy
import time

#You will need to get these from twitter and keep them SECRET! Apply for a developer account and follow the instructions.
consumer_key = 
consumer_secret = 
key = 
secret = 

#The tweepy documentation is a must read and you will find the code below there.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

#Input hashtag you are targeting.
hashtag = 

#Input amount of tweets you want tyo engage with. Keep it reasonable to stay within rate limits.
tweetnumber = 

tweets = tweepy.Cursor(api.search, hashtag).items(tweetnumber)

#Function to engage user's twitterbot with other twitter users. The tweepy documentation shows you different ways to engage.
def search_bot():
	for tweet in tweets:
		try:
			api.create_favorite(tweet.id)
			
			
		except tweepy.TweepError as e:
			print(e.reason)
			
#Call function. Rinse. Repeat. Enjoy.
search_bot()
