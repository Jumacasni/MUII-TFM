import desinfo_spread.twitter as twitter
import tweepy
import json

if __name__ == "__main__":
	api = twitter.auth()

	# My info
	data = api.me()
	# print(json.dumps(data._json, indent=2))

	# User's info
	data_nike = api.get_user("nike")
	# print(json.dumps(data_nike._json, indent=2))

	# User's followers length (20 by default)
	followers = api.followers(screen_name="nike")
	# print(len(followers))

	# 100 user's followers
	for user in tweepy.Cursor(api.followers, screen_name="nike").items(100):
		pass
		# print(json.dumps(user._json, indent=2))

	# User's followees
	for user in tweepy.Cursor(api.friends, screen_name="nike").items(100):
		pass
		# print(json.dumps(user._json, indent=2))

	# User's timeline
	for tweet in tweepy.Cursor(api.user_timeline, screen_name="nike", tweet_mode="extended").items(1):
		pass
		# print(json.dumps(tweet._json, indent=2))

	# Searchin tweets
	for tweet in tweepy.Cursor(api.search, q="twitter", tweet_mode="extended").items(10):
		pass
		# print(tweet._json["full_text"])