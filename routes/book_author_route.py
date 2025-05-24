from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.book_author_schema import Book_AuthorCreate,Book_AuthorOut
from sqlalchemy.orm import Session
from model.book import BookAuthor
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import book_author_repo

route=APIRouter(
    prefix="/author_book",
    tags=['author_book']
)


@route.get("/all",response_model=List[Book_AuthorOut])
def get_all_book_athor(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    book_author=book_author_repo.get_all_book_author(db=db)

    if not book_author:
        raise HTTPException(status_code=404,detail="Not Found")
    book_author:Book_AuthorCreate
    return book_author
    