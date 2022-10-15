from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from Auth.auth_db import User

engine = create_engine("sqlite:///User/user_feed/db/user.db", future=True)

Base = declarative_base()


class Blog(Base):
     __tablename_ = "blog"
     blog_id = Column(String, primary_key=True)
     user_id = Column(String, ForeignKey("media.user_id"))
     title = Column(String)
     description = Column(String)
     filename = Column(String, ForeignKey("media.filename"))


class Media(Base):

    __tablename__ = "media"
    filename = Column(String, primary_key=True)
    user_id = Column(String)
    filetype = Column(String)

    