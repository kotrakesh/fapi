from fastapi import Depends, FastAPI
from pydantic import UUID4
from . import crud, models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from os import environ as env




app = FastAPI()

#cors
origins = [env["ALLOWED_CROSS_ORIGIN_HOST"]]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"api home": "Hello posts, got t "}

@app.get("/posts",response_model=list[schemas.Post])
async def read_posts(skip: int = 0, limit: int = 100, db:Session=Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.get("/posts/{post_id}",response_model=schemas.Post | None)
async def read_post(post_id:UUID4,db:Session=Depends(get_db)):
    post = crud.get_post_by_id(db,id=post_id)
    return post

@app.post("/posts",response_model=schemas.Post | None)
async def add_post(postObj:schemas.PostCreateObj,db:Session=Depends(get_db)):
    post = crud.create_post(db,postObj.post)
    return post

@app.put("/posts/{post_id}",response_model= schemas.Post | None)
async def update_post(post_id:UUID4,post:schemas.PostCreate,db:Session=Depends(get_db)):
    post = crud.update_post(db,post_id,post)
    return  post

@app.delete("/posts/{post_id}", response_model= bool |  None)
async def delete_post(post_id:UUID4,db:Session=Depends(get_db)):
    post = crud.delete_post(db,post_id)
    return post