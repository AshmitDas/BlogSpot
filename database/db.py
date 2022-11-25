from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, TIMESTAMP
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import FetchedValue
from sqlalchemy.sql import func

engine = create_engine("sqlite:///database/db/user.db", future=True, connect_args={"check_same_thread": False})

Base = declarative_base()


class User(Base):
    """Creates the User credintials Table"""
    __tablename__ = "user"
    user_id = Column(String, primary_key=True)
    password = Column(String)  
    firstname = Column(String)
    lastname = Column(String)
    session_id = Column(String)
    

class Blog(Base):
     __tablename__ = "blog"
     fetch_id = Column(Integer, primary_key=True, autoincrement=True)
     user_id = Column(String, ForeignKey("user.user_id"))
     title = Column(String)
     description = Column(String)
     time_created = Column(TIMESTAMP, server_default=func.now())
     time_updated = Column(TIMESTAMP, onupdate=func.now())
     filename = Column(String)
     filetype = Column(String)

Base.metadata.create_all(engine)