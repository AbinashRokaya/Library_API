from fastapi import Depends,status,HTTPException
from database.database import get_db
from sqlalchemy.orm import Session
from typing import List
from schema.book_Category import BookCategoryCreate,BookCategoryOut,BookUpdateRequest
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


def category_by_name(category_name:str,db:Session):
    result=db.query(BookCategory).filter(BookCategory.category_name.like(f"%{category_name}%")).all()
    if not result:
        raise HTTPException(status_code=404,detail=f"category name {category_name} is not found")

    return result


def category_update(category_id:int,category_name:BookUpdateRequest,db:Session):
    category=db.query(BookCategory).filter(BookCategory.category_id==category_id).first()

    if not category:
        raise HTTPException(status_code=404,detail=f"Category id {category_id } is not found")
    
    update_data=category_name.dict(exclude_unset=True)

    for  key,value in update_data.items():
        setattr(category,key,value)

    db.commit()
    db.refresh(category)

    return category
    