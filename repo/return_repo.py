from fastapi import Depends,status,HTTPException
from datetime import datetime, date
from sqlalchemy.orm import Session
from typing import List
from schema.return_schema import BookReturnsCreate,BookReturnsResponse,BookReturnsResponse_1
from model.book import Book,BookBorrowers,BookReturns
from datetime import date,timedelta
from schema.transactionlogs_schema import TransactionLogCreate,TransactionLogResponse
from model.staff import Staff
from model.transactionlogs import Transactionlogs
from model.student import Student
from schema.token_shema import SystemUser

today=date.today()


from datetime import datetime

def total_fine_amount(return_date, release_date, due_date):
    # Convert to date if needed
    if isinstance(return_date, datetime):
        return_date = return_date.date()
    if isinstance(release_date, datetime):
        release_date = release_date.date()
    if isinstance(due_date, datetime):
        due_date = due_date.date()

    # If returned late
    if return_date > due_date:
        overdue_days = (return_date - due_date).days
        fine_amount = overdue_days * 10
    else:
        fine_amount = 0

    return fine_amount


def create_book_return(book_return:BookReturnsCreate,db:Session,current_user:SystemUser)->BookReturnsResponse_1:

    student=db.query(Student).filter(Student.stud_id==book_return.student_id).first()
    if student is None:
        raise HTTPException(status_code=404,detail=f"studetn id {book_return.student_id} is not found")
    
    ### Check the Staff
    staff=db.query(Staff).filter(Staff.name==current_user.username).first()
    if staff is None:
        raise HTTPException(status_code=404,detail=f"Staff is Not Found")
    
    return_book_list=[]
    not_book_foud_list=[]
 
    msg={"return book":[],"not borrow book":[],"not found":[]}
    for return_book_id in book_return.return_book:
        book=db.query(Book).filter(Book.book_id==return_book_id.book_id).first()
        if book:
            book_borrowers=db.query(BookBorrowers).filter(BookBorrowers.book_id==return_book_id.book_id,
                                                  BookBorrowers.stud_id==student.stud_id).first()
            if book_borrowers:
                return_book_list.append(book_borrowers.borrowers_id)
            else:
                msg["not borrow book"].append(f"book id {book.book_id} is borrowed by you")
        else:
            msg["not found"].append(f"book id {return_book_id.book_id} is not found")
    total_fine=0
    for borrower in return_book_list:
        book_borrowers=db.query(BookBorrowers).filter(BookBorrowers.borrowers_id==borrower).first()
       
        fine=total_fine_amount(today,book_borrowers.release_date,book_borrowers.due_date)
        total_fine+=fine


        new_return_books=BookReturns(
            borrowers_id=borrower,
            return_date=today,
            fine_amount=fine
        )
        db.add(new_return_books)


    
        book=db.query(Book).filter(Book.book_id==borrower).first()
        book.copies+=1
        return_log=Transactionlogs(
            book_id=book.book_id,
            stud_id=student.stud_id,
            action='return',
            transaction_date=today,
            staff_id=staff.staff_id,
        )
        db.delete(book_borrowers)
        db.add(return_log)
        msg["return book"].append(f"Returned Book ID {book_borrowers.book_id}, Fine: {fine}")

    db.commit()  # Single commit at the end

    return BookReturnsResponse_1(msg=msg, fine_amount=total_fine)