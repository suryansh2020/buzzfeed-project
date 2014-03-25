import json

#with open('AP.txt') as user_info:
#    user_info = json.loads(user_info)

user_info = open('AP.txt').read()


def iload_json(f, decoder=None, _w=json.decoder.WHITESPACE.match):
	
	decoder = decoder or json._default_decoder
	idx = _w(f, 0).end()
	end = len(f)

	try:
		while idx != end:
			(val, idx) = decoder.raw_decode(f, idx=idx)
			yield val
			idx = _w(f, idx).end()
	except ValueError as exc:
		raise ValueError('%s (%r at position %d).' % (exc, f[idx:], idx))

# In each object, 200 tweets.

ap_json = list(iload_json(user_info))

for item in ap_json[10][1].keys():
	print item + ':', ap_json[10][1][item]