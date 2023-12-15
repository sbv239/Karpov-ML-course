from database import Base, SessionLocal
from sqlalchemy.orm import relationship
from table_post import Post
from table_user import User
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime

class Feed(Base):
    __tablename__ = "feed_action"
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True, name="user_id")
    user = relationship("User")
    post_id = Column(Integer, ForeignKey(Post.id), primary_key=True, name="post_id")
    post = relationship("Post")
    action = Column(String)
    time = Column(DateTime)