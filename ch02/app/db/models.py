from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)

    def __repr__(self):
        return f'id = {self.id}, username = {self.username}'

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")


