from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.author_schema import AuthorCreate,AuthorOut,AuthorUpdate
from sqlalchemy.orm import Session
from model.book import Author
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import author_repo

route=APIRouter(
    prefix="/author",
    tags=['author']
)

@route.post("/add",response_model=AuthorOut)
def author_create(author:AuthorCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    new_author=author_repo.create_author(author=author,db=db)
    

    return new_author


@route.get("/all",response_model=List[AuthorOut])
def get_all_author(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_author=db.query(Author).all()

    if not all_author:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_author
    

@route.patch("/update/{author_id}")
def update_author(author_id:int,author_value:AuthorUpdate,db:Session=Depends(get_db)):

    return author_repo.update_author(author_id=author_id,auhtor_value=author_value,db=db)
