from fastapi import Depends,status,HTTPException
from datetime import date,timedelta
from sqlalchemy.orm import Session
from typing import List
from schema.return_schema import BookReturnsCreate,BookReturnsResponse
from model.book import Book,BookBorrowers,BookReturns
from datetime import date,timedelta
from schema.transactionlogs_schema import TransactionLogCreate,TransactionLogResponse
from model.staff import Staff
from model.transactionlogs import Transactionlogs
from model.student import Student
from schema.token_shema import SystemUser

today=date.today()


def total_fine_amount(return_date,release_date,due_date):
    return_book_day=abs(return_date-release_date)

    if return_book_day >due_date:
        fine_amount=return_book_day*10

    else:
        fine_amount=0

    return fine_amount


def create_book_return(book_return:BookReturnsCreate,db:Session,current_user:SystemUser)->BookReturnsResponse:
    book_borrowers=db.query(BookBorrowers).filter(BookBorrowers.borrowers_id==book_return.borrowers_id).first()
    staff=db.query(Staff).filter(Staff.email==current_user).first()
    student=db.query(Student).filter(Student.stud_id==book_borrowers.stud_id).first()
    

    if book_borrowers is None:
        raise HTTPException(status_code=404,detail=f"Book borrowers id {book_return.borrowers_id} is not found")
    
    fine=total_fine_amount(today,book_borrowers.release_date,book_borrowers.due_date)


    new_return_books=BookReturns(
        borrowers_id=book_return.borrowers_id,
        return_date=today,
        fine_amount=fine
    )
    db.add(new_return_books)


  
    book=db.query(Book).filter(Book.book_id==book_borrowers.book_id).first()
    book.copies+=1
    return_log=Transactionlogs(
        book_id=book.book_id,
        stud_id=student.stud_id,
        action='return',
        transaction_date=today,
        staff_id=staff.staff_id,
    )
    db.add(return_log)
    db.commit()
    db.refresh(new_return_books)

    return BookReturnsResponse(return_id=new_return_books.return_id,
                               borrowers_id=new_return_books.borrowers_id,
                               return_date=new_return_books.return_date,
                               fine_amount=new_return_books.fine_amount)





    
