from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.book_shema import BookCategoryCreate
from schema.book_Category import BookCategoryOut,BookUpdateRequest
from sqlalchemy.orm import Session
from model.book import BookCategory
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import book_category_repo

route=APIRouter(
    prefix="/category",
    tags=['category']
)

@route.post("/add")
def category_create(category:BookCategoryCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    cate=db.query(BookCategory).filter(BookCategory.category_name==category.category_name).first()
    if cate:
        raise HTTPException(status_code=400,detail="Category name alredy exists") 

    new_category=BookCategory(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return {"message":"New category is added"}


@route.get("/all",response_model=List[BookCategoryOut])
def get_all_category(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_category=db.query(BookCategory).all()

    if not all_category:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_category
    

@route.get("/{category_name}")
def get_category_by_name(category_name:str,db:Session=Depends(get_db)):
    return book_category_repo.category_by_name(category_name=category_name,db=db)

@route.patch("/update/{category_id}")
def update_category(category_id:int,catetory_name:BookUpdateRequest,db:Session=Depends(get_db)):
    return book_category_repo.category_update(category_id=category_id,category_name=catetory_name,db=db)
