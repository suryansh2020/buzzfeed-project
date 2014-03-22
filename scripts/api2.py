import oauth2 as oauth
import json
import urllib2
import time

def tweets(username, count, max_id=''):
	consumer_key = 'hi8NdkCukk9smiSznv09kw'
	consumer_secret = 'GZWvYvF7rSRN3QDO3qSFbIsfrPrbnU2BG59tfCaE'
	access_token = '321666686-bSpt0wXlhMfN8GMnL0ckMoEFszswcl4fhCTP273g'
	access_secret = 'utnIce1hMPAEZgAsRTKeVnm0qzmBzV4o0t8dj5PtY'

	consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
	token = oauth.Token(key=access_token, secret=access_secret)
	client = oauth.Client(consumer, token)

	if max_id:
		header, response = client.request('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + username + '&count=' + count + '&max_id=' + max_id, method="GET")
	else:
		header, response = client.request('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + username + '&count=' + count, method="GET")

	data = json.loads(response)[0]
	header = json.loads(header)
	
	time.sleep(3)
	return header

print tweets('buzzfeed', '2')
