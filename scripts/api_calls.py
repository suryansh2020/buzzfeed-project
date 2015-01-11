import oauth2 as oauth
import json
import urllib2
import time
import os

# User lookup/Twitter API
def twitter_api():
        consumer_key = os.environ['CONSUMER_KEY']
        consumer_secret = os.environ['CONSUMER_SECRET']
        access_token = os.environ['ACCESS_TOKEN']
        access_secret = os.environ['ACCESS_SECRET']

	consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
	token = oauth.Token(key=access_token, secret=access_secret)
	client = oauth.Client(consumer, token)

	usernames = open('../data/usernames.txt', 'rU')
	user_data = open('../data/user_data.txt', 'w')
	ids = open('../data/twitter_ids.txt', 'w')

	for user in usernames:
		header, response = client.request('https://api.twitter.com/1.1/users/lookup.json?screen_name=' + user, method="GET")
		data = json.loads(response)

		# For Twitter counter lookup
		twitter_id = json.dumps(data['id'])
		ids.write(str(twitter_id) + "\n")

		user_data.write(json.dumps(data, indent=0))
		print data['id'], 'done'
		time.sleep(3)


# Twittercounter API
def twittercounter_api():
	twitter_ids = open('../data/twitter_ids.txt', 'rU')
	twittercounter_data = open('../data/twittercounter_data.txt', 'w')

	for user_id in twitter_ids:
		response = urllib2.urlopen('http://api.twittercounter.com/?apikey=cdcf8e41037b706a523fc01a845c8b9d&twitter_id=' + user_id)
		data = json.load(response)

		twittercounter_data.write(json.dumps(data, indent=0))
		print user_id, 'done'
		time.sleep(3)

# Bitly api
def bitly_api():
	# Bitly calls go here
