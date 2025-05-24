from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.student_schema import StudentCreate,StudentOut
from sqlalchemy.orm import Session
from model.student import Student  
from typing import List
from auth.auth_dependancy import get_current_user
from schema.token_shema import SystemUser
from repo import student_repo

route=APIRouter(
    prefix="/student",
    tags=['student']
)

@route.post("/add")
def student_create(student:StudentCreate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    new_student=student_repo.create_student(student,db=db)
   
    return {"message":"New Student is added"}


@route.get("/all",response_model=List[StudentOut])
def get_all_student(db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user)):
    all_student=db.query(Student).all()

    if not all_student:
        raise HTTPException(status_code=404,detail="Not Found")
    
    return all_student
    