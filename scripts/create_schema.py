from sqlalchemy import *
from database import *

usernames = open('../data/usernames.txt', 'rU')
table_list = []

for name in usernames:
	test = Table(name.strip(), metadata, Column('id', Integer, primary_key=True), Column('text', String(300)), Column('favorite_count', Integer), Column('is_RT', String(10)), Column('RT_count', Integer), Column('date', DateTime))
	table_list.append(test)

metadata.create_all(engine)

