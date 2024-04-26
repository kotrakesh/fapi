from pydantic import BaseModel,UUID4
from datetime import datetime


class PostBase(BaseModel):
    title: str
    image_url: str | None = None
    content: str | None = None
    lat: float | None = None
    long: float | None = None



class PostCreate(PostBase):
    pass

class Post(PostBase):
    id:UUID4
    created_at:datetime | None = None
    updated_at:datetime | None = None
    class Config:
        from_attributes  = True


class PostCreateObj(BaseModel):
    post:PostCreate       