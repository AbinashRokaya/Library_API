from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime
from typing import List


class BookBorrowersBase(BaseModel):
    book_id:int
    
    release_date:datetime
    due_date:datetime


class BookBorrowersCreate(BaseModel):
    student_id:int
    Book_borrowers:List[BookBorrowersBase]


class BookBorrowersResponse(BookBorrowersBase):
    borrowers_id:int

    class Config:
        orm_mode=True


class BookBorrowersUpdate(BaseModel):
    book_id:Optional[int]
    stud_id:Optional[int]
    release_date:Optional[datetime]
    due_date:Optional[datetime]