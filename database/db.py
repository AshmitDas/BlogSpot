from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import FetchedValue
from sqlalchemy.sql import func

engine = create_engine("mysql+pymysql://BlogSpotDB:canine3_coat_rewire@localhost/USER?charset=utf8mb4", future=True)
# username = BlogSpotDB  password: canine3_coat_rewire
# connect_args={"check_same_thread": False}


Base = declarative_base()


class User(Base):
    """Creates the User credintials Table"""
    __tablename__ = "user"
    user_id = Column(String(15), primary_key=True)
    password = Column(String(50))  
    firstname = Column(String(10))
    lastname = Column(String(10))
    session_id = Column(String(50))
    

class Blog(Base):
     __tablename__ = "blog"
     fetch_id = Column(Integer, primary_key=True, autoincrement=True)
     user_id = Column(String(15), ForeignKey("user.user_id"))
     title = Column(String(100))
     description = Column(String(500))
     time_created = Column(TIMESTAMP, server_default=func.now())
     time_updated = Column(TIMESTAMP, onupdate=func.now())
     filename = Column(String(200))
     filetype = Column(String(200))

Base.metadata.create_all(engine)