from fastapi import Depends,status,HTTPException
from datetime import date,timedelta
from sqlalchemy.orm import Session
from typing import List
from schema.book_borrowers_schema import BookBorrowersCreate,BookBorrowersResponse
from model.book import Book,BookBorrowers
from model.student import Student
from model.transactionlogs import Transactionlogs
from schema.transactionlogs_schema import TransactionLogCreate,TransactionLogResponse
from model.staff import Staff
from schema.token_shema import SystemUser
from typing import List

today=date.today()
future_date=today+timedelta(days=15)
def create_book_borrowers(book_borrowers:BookBorrowersCreate,db:Session,current_user:SystemUser)->BookBorrowersResponse:
    ### Check the Student id 
    student=db.query(Student).filter(Student.stud_id==book_borrowers.student_id).first()
    if student is None:
        raise HTTPException(status_code=404,detail=f"studetn id {book_borrowers.student_id} is not found")
    
    ### Check the Staff
    staff=db.query(Staff).filter(Staff.name==current_user.username).first()
    if staff is None:
        raise HTTPException(status_code=404,detail=f"Staff is Not Found")

    
    ###  Make the list of book if present or borrower
    Book_list_id=[]
    Not_book_list=[]
    book_already_borrow=[]
    no_copies_book_found=[]
    for book in book_borrowers.Book_borrowers:
        book_present=db.query(Book).filter(Book.book_id==book.book_id).first()
        if book_present:
            check_book_double = db.query(BookBorrowers).filter(
            BookBorrowers.book_id == book_present.book_id,
            BookBorrowers.stud_id == student.stud_id).first()
            if book_present.copies <=0:
                no_copies_book_found.append(book_present.book_id)
            
            else:
                if check_book_double:
                    book_already_borrow.append(book_present.book_id)
                else:

                    Book_list_id.append(book_present.book_id)
        else:
            Not_book_list.append(book.book_id)

    for present_book in Book_list_id:
        any_copy_of_book=db.query(Book).filter(Book.book_id==present_book).first()

        new_book_borrowers=BookBorrowers(book_id=present_book,
                                        stud_id=student.stud_id,
                                        release_date=today,
                                        due_date=future_date
                                        )
        
        db.add(new_book_borrowers)
        staff_id = staff.staff_id
        borrower_log=Transactionlogs(
            book_id=present_book,
            stud_id=student.stud_id,
            action='borrow',
            transaction_date=today,
            staff_id=staff_id,
        )

        db.add(borrower_log)
        any_copy_of_book.copies-=1
    
        db.commit()
        db.refresh(any_copy_of_book)
        db.refresh(new_book_borrowers)

    
    
    return BookBorrowersResponse(borrowers_id=new_book_borrowers.borrowers_id,
                                 book_id=new_book_borrowers.book_id,
                                     stud_id=new_book_borrowers.stud_id,
                                     release_date=today,
                                     due_date=future_date
                                 )
