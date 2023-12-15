from sqlalchemy import func
from database import SessionLocal
from fastapi import FastAPI, Depends, HTTPException
from schema import UserGet, PostGet, FeedGet
from table_post import Post
from table_user import User
from table_feed import Feed
from typing import List
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        return db
    
@app.get("/user/{id}", response_model=UserGet)
def get_user_id(id : int, db : Session = Depends(get_db)):
    result = db.query(User).filter(User.id == id).one_or_none()
    if not result:
        raise HTTPException(404)
    return result

@app.get("/post/{id}", response_model=PostGet)
def get_post_id(id : int, db : Session = Depends(get_db)):
    result = db.query(Post).filter(Post.id == id).one_or_none()
    if not result:
        raise HTTPException(404)
    return result

@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_feed(id : int, limit : int = 10, db : Session = Depends(get_db)):
    result = db.query(Feed).filter(Feed.post_id == id).order_by(Feed.time.desc()).limit(limit).all()
    return result

@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_feed(id : int, limit : int = 10, db : Session = Depends(get_db)):
    result = db.query(Feed).filter(Feed.user_id == id).order_by(Feed.time.desc()).limit(limit).all()
    return result

@app.get("/post/recommendations/", response_model=List[PostGet])
def get_post_recommendations(limit : int = 10, db : Session = Depends(get_db)):
    result = db.query(Post).select_from(Feed).filter(Feed.action == 'like').join(Post).group_by(Post.id).order_by(func.count(Post.id).desc()).limit(limit).all()
    return result