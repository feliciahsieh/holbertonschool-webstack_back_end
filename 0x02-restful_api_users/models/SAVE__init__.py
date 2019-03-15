# mysqlclient (a maintained fork of MySQL-Python)
from models.user import User
from models.base_model import BaseModel
from models.base_model import Base

import os
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# connect to server
host = os.getenv('HBNB_YELP_MYSQL_HOST')
user = os.getenv('HBNB_YELP_MYSQL_USER')
passw = os.getenv('HBNB_YELP_MYSQL_PWD')
db = os.getenv('HBNB_YELP_MYSQL_DB')
env = os.getenv('HBNB_YELP_ENV')

db_engine = sqlalchemy.create_engine(
    'mysql+mysqldb://{}:{}@{}/{}'.format(user, passw, host, db))

if env == 'test':
    Base.metadata.drop_all(bind=db_engine)

Base.metadata.create_all(db_engine)


# expire_on_commit flag is Needed on the sessionmaker to avoid expiring object
# once you commit. An expired object will need to be refreshed from the
# database before accessing a property thus it needs to be in a session scope.
# Without expiring it, you can access properties out of the session scope.
session_factory = sessionmaker(bind=db_engine, expire_on_commit=False)
Session = scoped_session(session_factory)
db_session = Session()
