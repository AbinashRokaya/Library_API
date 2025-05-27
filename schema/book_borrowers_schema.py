from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime
from typing import List,Dict


class BookBorrowersBase(BaseModel):
    book_id:int
    


class BookBorrowersCreate(BaseModel):
    student_id:int
    Book_borrowers:List[BookBorrowersBase]


class BookBorrowersResponse(BookBorrowersBase):
    borrowers_id:int

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