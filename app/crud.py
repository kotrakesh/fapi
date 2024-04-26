from http.client import HTTPException
from sqlalchemy.orm import Session
from . import schemas,models

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post_by_id(db:Session,id:models.Post.id):
    return db.query(models.Post).filter(models.Post.id==id).first()

def update_post(db:Session,id:models.Post.id,post:schemas.PostCreate):
        db_post=db.query(models.Post).filter_by(id=id).first()
        if not post:
            raise HTTPException(status_code=422, detail="data not")
        db_post.title = post.title
        db_post.content = post.content
        db_post.image_url = post.image_url  # Update additional field
        db_post.lat = post.lat  # Update additional field
        db_post.long = post.long  # Update additional field
        db.commit()
        db.refresh(db_post)
        return db_post

def delete_post(db: Session ,id: models.Post.id ):
    db_post = db.query(models.Post).filter_by(id=id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return True