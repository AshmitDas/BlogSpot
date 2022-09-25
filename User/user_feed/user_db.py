from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///User/user_feed/db/user.db", future=True)

Base = declarative_base()

class Text(Base):

     __tablename__ = "text"
     text_id = Column(Integer, primary_key=True)
     body = Column(String)
     user_id = Column(String)

class Media(Base):

    __tablename__ = "media"
    filename = Column(String, primary_key=True)
    user_id = Column(String)
    filetype = Column(String)

    