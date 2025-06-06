from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime
from schema.book_Category import BookCategoryCreate
from schema.publisher import PublisherCreate
from schema.author_schema import AuthorCreate



class book_description(BaseModel):
    book_id:int
    title:str
    edition:str
    cost:float
    copies:int
    status:Status

class book_description_1(BaseModel):

    title:str
    edition:str
    cost:float
    copies:int
    status:Status

class BookResponse(BaseModel):
    title:Optional[str]=None
    edition:Optional[str]=None
    cost:Optional[float]=None
    copies:Optional[int]=None
    status:Optional[Status]=None

    class Config:
        orm_mode=True




class BookBase(BaseModel):

    description:book_description_1
    category:BookCategoryCreate
    publisher:PublisherCreate
    author:AuthorCreate

class BookCreate_1(BaseModel):
    description:book_description_1
    category_id:int
    publisher_id:int

class BookCreateResponse(BookBase):
    pass


class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title:Optional[str]=None
    edition:Optional[str]=None
    cost:Optional[float]=None
    copies:Optional[int]=None
    status:Optional[Status]=None
    
    

class BookOut(BookBase):
    book_id:int

    class Config:
        orm_mode=True





class BookCategoryUpdate(BaseModel):
     category_name:Optional[str]=None



                  

