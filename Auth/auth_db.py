from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///Auth/db/auth.db", future=True)

Base = declarative_base()

class User(Base):
    """Creates the User credintials Table"""
    __tablename__ = "user"
    user_id = Column(String, primary_key=True)
    password = Column(String)  
    firstname = Column(String)
    lastname = Column(String)

Base.metadata.create_all(engine)