from sqlalchemy import Boolean,Column,  String,UUID,Float,DATETIME,TIMESTAMP, func,text
from sqlalchemy.orm import relationship

from .database import Base

class Post(Base):
    __tablename__="posts"

    id= Column(UUID,
               server_default=text("uuid_generate_v4()"),
               primary_key=True)
    title = Column(String)
    image_url = Column(String)
    content = Column(String)
    lat = Column(Float)
    long = Column(Float)
    created_at =Column(TIMESTAMP,server_default=func.now())
    updated_at = Column(TIMESTAMP,server_default=func.now())

