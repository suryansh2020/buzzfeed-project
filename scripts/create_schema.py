from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_session
from sqlalchemy import *

engine = create_engine('postgresql://postgres:m0rg3ns0nn3@localhost:5432/twitter_data')

Base = declarative_base()

class Table(Base):
	__tablename__ = 'WashingtonPost'

	id = Column(Integer, primary_key=True)
	text = Column(String)
	favorite_count = Column(Integer)
	is_RT = Column(String)
	RT_count = Column(Integer)
	date = Column(DateTime)

	def __init__(self, name, age):
		self.text = text
		self.favorite_count = favorite_count
		self.is_RT = is_RT
		self.RT_count = RT_count
		self.date = date

Base.metadata.create_all(engine)

