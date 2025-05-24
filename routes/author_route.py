from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.author_schema import AuthorCreate,AuthorOut
from sqlalchemy.orm import Session
from model.book import Author
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser

route=APIRouter(
    prefix="/author",
    tags=['author']
)

@route.post("/add")
def author_create(author:AuthorCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    authors=db.query(Author).filter(Author.author_name==author.author_name).first()
    if authors:
        raise HTTPException(status_code=400,detail="Author name alredy exists") 

    new_author=Author(**author.model_dump())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    return {"message":"New author is added"}


@route.get("/all",response_model=List[AuthorOut])
def get_all_author(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_author=db.query(Author).all()

    if not all_author:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_author
    