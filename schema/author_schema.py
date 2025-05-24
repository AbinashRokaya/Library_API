from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime


class AuthorBase(BaseModel):
    author_name:str

class AuthorCreate(AuthorBase):
    pass

class AuthorOut(AuthorBase):
    author_id:int

    class Config:
        orm_mode=True

class AuthorUpdate(BaseModel):
    author_name:Optional[str]

