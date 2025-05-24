from fastapi import Depends,status,HTTPException
from sqlalchemy.orm import Session
from typing import List
from schema.author_schema import AuthorCreate,AuthorOut
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
