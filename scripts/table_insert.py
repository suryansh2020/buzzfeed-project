from sqlalchemy import *
from database import *
import os
import json

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


# Too many loops
for f in os.listdir('../json'):
	table = f[:-4]
	filename = os.path.join('../json', f)
	json_data = open(filename).read()

	data = list(iload_json(json_data))
	flat = [item for sublist in data for item in sublist]

	tablename = metadata.tables[table]
	inserting = tablename.insert()
	print inserting
	# data[n][n]['text']
	#for item in flat:
	#	print item['text']

	break

