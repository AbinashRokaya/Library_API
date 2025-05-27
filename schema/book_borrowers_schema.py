from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime
from typing import List,Dict
from schema.book_shema import BookResponse


class BookBorrowersBase(BaseModel):
    book_id:int
    
    


class BookBorrowersCreate(BaseModel):
    student_id:int
    Book_borrowers:List[BookBorrowersBase]


class BookBorrowersResponse(BaseModel):
    borrowers_id:Optional[int]=None
    Book:Optional[BookResponse]=None

    class Config:
        orm_mode=True

class BookBorrowesResponse_1(BaseModel):
    msg:Optional[Dict[str,List[str]]]

    class Config:
        orm_mode=True


class BookBorrowersUpdate(BaseModel):
    book_id:Optional[int]
    stud_id:Optional[int]

    msg:List[str]