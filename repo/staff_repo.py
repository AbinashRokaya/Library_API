from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.staff_shema import StaffOut,StaffCreate
from sqlalchemy.orm import Session
from model.staff import Staff 
from typing import List
from auth.auth_dependancy import get_current_user
from auth.hashing import get_password_hashed


def staff_create(staff:StaffCreate,db:Session):
    staffs=db.query(Staff).filter(Staff.name==staff.name).first()
    if staffs:
        raise HTTPException(status_code=400,detail="Staff name alredy exists")
     
    hash_password=get_password_hashed(staff.password)
    new_staff=Staff(name=staff.name,
                    contract=staff.contract,
                    email=staff.email,
                    address=staff.address,
                    password=hash_password,
                    role=staff.role
                    )
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)

    return {"message":"New staff is added"}

def get_staff_by_id(staff_id:int,db:Session)->StaffOut:
    staff=db.query(Staff).filter(Staff.staff_id==staff_id).first()
    if not staff:
        raise HTTPException(status_code=404,detail="staff id {staff_id} is not found")
    
    detail_staff=StaffOut(staff_id=staff.staff_id,
                        name=staff.name,
                        contract=staff.contract,
                        email=staff.email,
                        address=staff.address,
                        role=staff.role)
    

    return detail_staff



