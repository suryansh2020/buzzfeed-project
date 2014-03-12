import oauth2 as oauth
import json
import time

# User lookup/Twitter API
   
consumer_key = 'hi8NdkCukk9smiSznv09kw'
consumer_secret = 'GZWvYvF7rSRN3QDO3qSFbIsfrPrbnU2BG59tfCaE'
access_token = '321666686-bSpt0wXlhMfN8GMnL0ckMoEFszswcl4fhCTP273g'
access_secret = 'utnIce1hMPAEZgAsRTKeVnm0qzmBzV4o0t8dj5PtY'

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
token = oauth.Token(key=access_token, secret=access_secret)
client = oauth.Client(consumer, token)

usernames = open('usernames.txt', 'rU')
user_data = open('user_data.txt', 'w')
ids = open('twitter_ids.txt', 'w')

for user in usernames:
	header, response = client.request('https://api.twitter.com/1.1/users/lookup.json?screen_name=' + user, method="GET")
	data = json.loads(response)[0]

	# For Twitter counter lookup
	ids.write(json.dumps(data['id'])), "\n"

	user_data.write(json.dumps(data)), "\n"
	print data['id'], 'done'
	time.sleep(3)