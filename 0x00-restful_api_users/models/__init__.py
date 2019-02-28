# mysqlclient (a maintained fork of MySQL-Python)
from models.base_model import Base, BaseModel
import os
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# connect to server
host = os.getenv('HBNB_YELP_MYSQL_HOST')
user = os.getenv('HBNB_YELP_MYSQL_USER')
pwd = os.getenv('HBNB_YELP_MYSQL_PWD')
db = os.getenv('HBNB_YELP_MYSQL_DB')
env = os.getenv('HBNB_YELP_ENV')

db_engine = sqlalchemy.create_engine(
    'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db))

if env == 'test':
    Base.metadata.drop_all(bind=db_engine)

Base.metadata.create_all(db_engine)

session_factory = sessionmaker(bind=db_engine, expire_on_commit=False)
Session = scoped_session(session_factory)
db_session = Session()
