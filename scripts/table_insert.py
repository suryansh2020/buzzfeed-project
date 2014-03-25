from sqlalchemy import *
from sqlalchemy.orm import create_session

engine = create_engine('postgresql://postgres:m0rg3ns0nn3@localhost:5432/twitterdata')

session = create_session(bind=engine)

