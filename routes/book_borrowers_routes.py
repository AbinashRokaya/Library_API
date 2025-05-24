from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.book_borrowers_schema import BookBorrowersCreate,BookBorrowersResponse
from sqlalchemy.orm import Session
from model.book import BookBorrowers
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import book_borrowers_repo
from typing import List

route=APIRouter(
    prefix="/borrowers",
    tags=['borrowers']
)

@route.post("/add")
def borrower_create(borrower:BookBorrowersCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    book_borrowers_repo.create_book_borrowers(borrower,db=db,current_user=current_user)

    return {"message":"New borrower is added"}


@route.get("/all",response_model=List[BookBorrowersResponse])
def get_all_borrower(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_borrower=db.query(BookBorrowers).all()

    if not all_borrower:
        raise HTTPException(status_code=404,detail="Not Found")
    return all_borrower
    