from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.return_schema import BookReturnsCreate,BookReturnsResponse
from sqlalchemy.orm import Session
from model.book import BookReturns,BookBorrowers
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import return_repo

route=APIRouter(
    prefix="/return",
    tags=['return']
)

@route.post("/add")
def book_return_create(book_return:BookReturnsCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    return_repo.create_book_return(book_return,db=db,current_user=current_user)

    return {"message":"New book return is added"}


@route.get("/all",response_model=List[BookReturnsResponse])
def get_all_book_return(db:Session=Depends(get_db)):
    all_book_return=db.query(BookReturns).all()

    if not all_book_return:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_book_return
    