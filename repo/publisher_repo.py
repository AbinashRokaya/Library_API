from fastapi import Depends,status,HTTPException
from database.database import get_db
from sqlalchemy.orm import Session
from typing import List
from schema.publisher import PublisherCreate,PublisherOut,PublisherUpdate
from model.book import Publisher

def create_publisher(publisher:PublisherCreate,db:Session)->PublisherOut:
    exist_publisher=db.query(Publisher).filter(publisher.publisher_name==publisher.publisher_name).first()

    if exist_publisher:
        get_publiher=PublisherOut(publisher_id=exist_publisher.publisher_id,
                              publisher_name=exist_publisher.publisher_name)
        
        return get_publiher
    
        
    new_publisher=Publisher(publisher_name=publisher.publisher_name)
    db.add(new_publisher)
    db.commit()
    db.refresh(new_publisher)

    get_publiher=PublisherOut(publisher_id=new_publisher.publisher_id,
                              publisher_name=new_publisher.publisher_name)
    
    return get_publiher


def update_publisher(publisher_id:int,publisher_value:PublisherUpdate,db:Session):
    publisher=db.query(Publisher).filter(Publisher.publisher_id==publisher_id).first()

    if not publisher:
        raise HTTPException(status_code=404,detail=f"Publisher id {publisher_id} is not found")
    
    update_data=publisher_value.dict(exclude_unset=True)


    for key,value in update_data.items():
        setattr(publisher,key,value)

    db.commit()
    db.refresh(publisher)

    return publisher