from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
