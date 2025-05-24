from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.publisher import PublisherCreate,PublisherOut

from sqlalchemy.orm import Session
from model.book import Publisher
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser

route=APIRouter(
    prefix="/Publisher",
    tags=['publisher']
)

@route.post("/add")
def publisher_create(publisher:PublisherCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    publishers=db.query(Publisher).filter(Publisher.publisher_name==publisher.publisher_name).first()
    if publishers:
        raise HTTPException(status_code=400,detail="Publisher name alredy exists") 

    new_publisher=Publisher(**publisher.model_dump())
    db.add(new_publisher)
    db.commit()
    db.refresh(new_publisher)

    return {"message":"New publisher is added"}


@route.get("/all",response_model=List[PublisherOut])
def get_all_publisher(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_publisher=db.query(Publisher).all()

    if not all_publisher:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_publisher
    