from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.staff_shema import StaffCreate,StaffOut
from sqlalchemy.orm import Session
from model.staff import Staff
from typing import List
from auth.hashing import get_password_hashed
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser

route=APIRouter(
    prefix="/staff",
    tags=['staff']
)

@route.post("/add")
def staff_create(staff:StaffCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
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


@route.get("/all",response_model=List[StaffOut])
def get_all_staff(db:Session=Depends(get_db)):
    all_staff=db.query(Staff).all()

    if not all_staff:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_staff