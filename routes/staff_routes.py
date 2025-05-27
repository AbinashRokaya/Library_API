from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.staff_shema import StaffCreate,StaffOut
from sqlalchemy.orm import Session
from model.staff import Staff
from typing import List
from auth.hashing import get_password_hashed
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import staff_repo

route=APIRouter(
    prefix="/staff",
    tags=['staff']
)

@route.post("/add")
def staff_create(staff:StaffCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    new_staff=staff_repo.staff_create(staff=staff,db=db)
    return new_staff


@route.get("/all",response_model=List[StaffOut])
def get_all_staff(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_staff=db.query(Staff).all()

    if not all_staff:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_staff

@route.get("/{staff_id}")
def get_staff_by_id(staff_id:int,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user))->StaffOut:
    staff_detail=staff_repo.get_staff_by_id(staff_id=staff_id,db=db)

    return staff_detail


