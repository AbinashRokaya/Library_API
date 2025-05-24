from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime



class BookReturnsBase(BaseModel):
    borrowers_id:int
    return_date:datetime
    fine_amount:float

class BookReturnsCreate(BookReturnsBase):
    pass

class BookReturnsResponse(BookReturnsBase):
    return_id:int

    class Config:
        orm_mode=True

class BookReturnsUpdate(BaseModel):
    borrowers_id:Optional[int]
    return_date:Optional[datetime]
    fine_amount:Optional[float]