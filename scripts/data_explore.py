import json

with open('../data/user_data.txt') as user_info:
    user_info = json.load(user_info)

print len(user_info)

