from fastapi import Depends,status,HTTPException

from sqlalchemy.orm import Session
from typing import List
from schema.book_shema import BookCreate,BookOut,BookCreate_1,book_description
from model.book import Book


def create_book(book:BookCreate_1,db:Session)->book_description:
    new_book=db.query(Book).filter(Book.title==book.description.title and Book.edition==book.description.edition).first()
    if new_book:
        raise HTTPException(status_code=400,detail="Book already exists")
    new_book_create=Book(title=book.description.title,
                        edition=book.description.edition,
                        cost=book.description.cost,
                        copies=book.description.copies,
                        status=book.description.status,
                        category_id=book.category_id,
                        publisher_id=book.publisher_id)
    
    db.add(new_book_create)
    db.commit()
    db.refresh(new_book_create)

    book_detail=book_description(
                        book_id=new_book_create.book_id,
                        title=new_book_create.title,
                        edition=new_book_create.edition,
                        cost=new_book_create.cost,
                        copies=new_book_create.copies,
                        status=new_book_create.status
    )
     
    return book_detail
     