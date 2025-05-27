from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.book_borrowers_schema import BookBorrowersCreate,BookBorrowersResponse,BookBorrowesResponse_1
from sqlalchemy.orm import Session
from model.book import BookBorrowers
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import book_borrowers_repo
from typing import List
from schema.book_shema import BookResponse
from model.book import Book

route=APIRouter(
    prefix="/borrowers",
    tags=['borrowers']
)

@route.post("/add")
def borrower_create(borrower:BookBorrowersCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user))->BookBorrowesResponse_1:
    book_borrower=book_borrowers_repo.create_book_borrowers(borrower,db=db,current_user=current_user)

    return book_borrower


@route.get("/{student_id}",response_model=List[BookBorrowersResponse])
def get_all_borrower(student_id:int,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_borrower=db.query(BookBorrowers).filter(BookBorrowers.stud_id==student_id).all()
    
    if not all_borrower:
        raise HTTPException(status_code=404,detail="Not Found")
    
    book_list_all=[]
    for book in all_borrower:
        book_list=db.query(Book).filter(Book.book_id==book.book_id).first()
        list=BookBorrowersResponse(borrowers_id=book.book_id,
                                   Book=BookResponse(
                                       title=book_list.title,
                                       edition=book_list.edition,
                                       cost=book_list.cost,
                                       copies=book_list.copies,
                                       status=book_list.status
                                   ))
        
        book_list_all.append(list)
    
    
    

    return book_list_all
    