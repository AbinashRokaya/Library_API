from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime
from typing import List,Dict


class BookReturnsBase(BaseModel):
    book_id:int

class BookReturnsCreate(BaseModel):
    student_id:int

    return_book:List[BookReturnsBase]

class BookReturnsResponse(BookReturnsBase):
    return_id:int

    class Config:
        orm_mode=True

class BookReturnsResponse_1(BaseModel):
    msg:Optional[Dict[str,List[str]]]
    fine_amount:Optional[int]

    class Config:
        orm_mode=True

class BookReturnsUpdate(BaseModel):
    borrowers_id:Optional[int]
    return_date:Optional[datetime]
    fine_amount:Optional[float]