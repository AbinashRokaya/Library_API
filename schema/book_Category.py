from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime

class BookCategoryBase(BaseModel):
    category_name:str


class BookUpdateRequest(BookCategoryBase):
     class Config:
        orm_mode=True
class BookCategoryCreate(BookCategoryBase):
    pass

class BookCategoryOut(BookCategoryBase):
    category_id:int

    class Config:
        orm_mode=True
