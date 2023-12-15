from database import Base, SessionLocal
from sqlalchemy import Column, String, Integer

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)

if __name__ == "__main__":
    session = SessionLocal()
    query = session.query(Post).filter(Post.topic == "business").order_by(Post.id.desc()).limit(10).all()
    result_list = [i.id for i in query]
    print(result_list)