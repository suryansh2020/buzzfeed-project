import oauth2 as oauth
import json
import urllib2
import time

# User lookup/Twitter API
def twitter_api():
	consumer_key = 'hi8NdkCukk9smiSznv09kw'
	consumer_secret = 'GZWvYvF7rSRN3QDO3qSFbIsfrPrbnU2BG59tfCaE'
	access_token = '321666686-bSpt0wXlhMfN8GMnL0ckMoEFszswcl4fhCTP273g'
	access_secret = 'utnIce1hMPAEZgAsRTKeVnm0qzmBzV4o0t8dj5PtY'

	consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
	token = oauth.Token(key=access_token, secret=access_secret)
	client = oauth.Client(consumer, token)

	usernames = open('../data/usernames.txt', 'rU')
	user_data = open('../data/user_data.txt', 'w')
	ids = open('../data/twitter_ids.txt', 'w')

	for user in usernames:
		header, response = client.request('https://api.twitter.com/1.1/users/lookup.json?screen_name=' + user, method="GET")
		data = json.loads(response)[0]

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