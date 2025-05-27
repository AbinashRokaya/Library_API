from fastapi import Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List
from schema.author_schema import AuthorCreate,AuthorOut,AuthorUpdate
from model.book import Author


def create_author(author:AuthorCreate,db:Session)->AuthorOut:
    old_author=db.query(Author).filter(Author.author_name==author.author_name).first()

    if old_author:
        get_author=AuthorOut(author_id=old_author.author_id,
                             author_name=old_author.author_name)
        
        return get_author
    
    new_author=Author(author_name=author.author_name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    get_author=AuthorOut(author_id=new_author.author_id,
                             author_name=new_author.author_name)
        
    
    return get_author


def update_author(author_id:int,auhtor_value:AuthorUpdate,db:Session):
    auhtor=db.query(Author).filter(Author.author_id==author_id).first()

    if not auhtor:
        raise HTTPException(status_code=404,detail=f"auhtor id {author_id} not found")
    
    update_data=auhtor_value.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(auhtor,key,value)

    db.commit()
    db.refresh(auhtor)

    return auhtor

    
