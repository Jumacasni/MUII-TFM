import tweepy
import desinfo_spread.config as config

def auth():
	"""
	auth does authenticate my user in order to use Twitter API

	:return api ready to use
	"""

	api_key = config.api_key
	api_secret = config.api_secret
	access_token = config.access_token
	access_token_secret = config.token_secret

	auth = tweepy.auth.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

	return api