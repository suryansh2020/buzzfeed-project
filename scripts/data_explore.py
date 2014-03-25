import json

#with open('AP.txt') as user_info:
#    user_info = json.loads(user_info)

user_info = open('../json/ABC.txt').read()


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

#print len(ap_json)

new_ap = [item for sublist in ap_json for item in sublist]

print len(new_ap)

for item in new_ap[10].keys():
	print item + ':', new_ap[10][item]