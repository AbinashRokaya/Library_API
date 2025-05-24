from fastapi import Depends,status
from database.database import get_db
from sqlalchemy.orm import Session
from typing import List
from schema.book_Category import BookCategoryCreate,BookCategoryOut
from model.book import BookCategory

def create_category(book_category:BookCategoryCreate,db:Session)->BookCategoryOut:
    exist_category=db.query(BookCategory).filter(BookCategory.category_name==book_category.category_name).first()

    if exist_category:
        get_category=BookCategoryOut(category_id=exist_category.category_id,
                              category_name=exist_category.category_name)
        return get_category
    
    book_category=BookCategory(category_name=book_category.category_name)
    db.add(book_category)
    db.commit()
    db.refresh(book_category)
    new_book_category=BookCategoryOut(category_id=book_category.category_id,
                                      category_name=book_category.category_name)

    return new_book_category