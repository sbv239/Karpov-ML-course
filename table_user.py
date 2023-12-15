from database import Base, SessionLocal
from sqlalchemy import Column, String, Integer, func

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(Integer)
    os = Column(String)
    source = Column(String)

if __name__ == "__main__":
    session = SessionLocal()
    res = session.query(User.country, User.os, func.count()).filter(User.exp_group == 3).group_by(User.country, User.os).having(func.count() > 100).order_by(func.count().desc()).all()
    print(res)