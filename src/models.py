import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name=Column(String(250),nullable=False)
    last_name =Column(String(250))
    email= Column(String(250) ,nullable=False)
    password=Column(String(250), nullable=False)

    following = relationship('Follower',back_populates = "user")


class Follower(Base):
    __tablename__= 'follower'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    user = relationship(User, back_populates="following")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



class Media(Base):
    __tablename__= ' media'
    id = Column(Integer, primary_key=True)
    media_url = Column (String(255))
    caption = Column (String(500))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship(User, back_populates="media")
    
    



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
