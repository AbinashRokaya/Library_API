from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.transactionlogs_schema import TransactionLogCreate,TransactionLogResponse
from sqlalchemy.orm import Session
from model.transactionlogs import Transactionlogs
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser

route=APIRouter(
    prefix="/transactionlog",
    tags=['transactionlog']
)

@route.post("/add")
def transactionlog_create(transactionlog:TransactionLogCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    transactionlogs=db.query(Transactionlogs).filter(Transactionlogs.book_id==transactionlog.book_ID).first()
    if transactionlogs:
        raise HTTPException(status_code=400,detail="Transactionlog name alredy exists") 

    new_transactionlog=Transactionlogs(**transactionlog.model_dump())
    db.add(new_transactionlog)
    db.commit()
    db.refresh(new_transactionlog)

    return {"message":"New transactionlog is added"}


@route.get("/all",response_model=List[TransactionLogResponse])
def get_all_transactionlog(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_transactionlog=db.query(Transactionlogs).all()

    if not all_transactionlog:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_transactionlog
    