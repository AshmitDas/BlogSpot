from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///database/db/user.db", future=True)

Base = declarative_base()


class User(Base):
    """Creates the User credintials Table"""
    __tablename__ = "user"
    user_id = Column(String, primary_key=True)
    password = Column(String)  
    firstname = Column(String)
    lastname = Column(String)
    session_id = Column(String)


class Media(Base):

    __tablename__ = "media"
    filename = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("user.user_id"))
    filetype = Column(String)

    

class Blog(Base):
     __tablename__ = "blog"
     blog_id = Column(String, primary_key=True)
     user_id = Column(String, ForeignKey("user.user_id"))
     title = Column(String)
     description = Column(String)
     filename = Column(String, ForeignKey("media.filename"))

Base.metadata.create_all(engine)