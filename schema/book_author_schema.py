from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime

class Book_AuthorBase(BaseModel):
    book_id:int
    author_id:int

class Book_AuthorCreate(Book_AuthorBase):
    pass

class Book_AuthorOut(Book_AuthorBase):
    class Config:
        orm_mode=True

