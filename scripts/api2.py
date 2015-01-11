import oauth2 as oauth
import json
import urllib2
import time
import os

def tweets(username, count, filename, max_id='', add=''):
	consumer_key = os.environ['CONSUMER_KEY']
	consumer_secret = os.environ['CONSUMER_SECRET']
	access_token = os.environ['ACCESS_TOKEN']
	access_secret = os.environ['ACCESS_SECRET']

	consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
	token = oauth.Token(key=access_token, secret=access_secret)
	client = oauth.Client(consumer, token)

	if max_id:
		header, response = client.request('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + username + '&count=' + count + '&max_id=' + max_id, method="GET")
	else:
		header, response = client.request('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=' + username + '&count=' + count, method="GET")

	
	if add == 'yes':
		data = json.loads(response)
		f = open(filename, 'a')
	else:
		data = json.loads(response)
		f = open(filename, 'w')

	last_id = str(data[-1]['id'])
	last_date = data[-1]['created_at']

	f.write(json.dumps(data, indent=0))
	time.sleep(10)
	return last_id, last_date

def continuing(user, filename):
	last_id, last_date = tweets(user, '200', filename)
	num_tweets = 200
	done = 'no'

	while done != 'yes':
		print last_id, last_date

		if num_tweets < 3200:

			if last_date[-4:] == '2014':

				if last_date[4:9] != 'Feb 1':
					last_id, last_date = tweets(user, '200', filename, max_id=last_id, add='yes')
					num_tweets += 200
				else:
					done = 'yes'
			else:
				done = 'yes'
		else:
			done = 'yes'

userlist = open('../data/usernames.txt', 'rU')

for u in userlist:
	u = u.strip()
	print u
	continuing(u, u + '.txt')
