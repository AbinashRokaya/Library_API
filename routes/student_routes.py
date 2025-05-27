from fastapi import APIRouter,Depends,HTTPException,status,Body
from database.database import get_db
from schema.student_schema import StudentCreate,StudentOut,GetStudentID,StudentUpdate
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
    

@route.get("/{id}",response_model=StudentOut)
def get_student_by_id(student=int,db:Session=Depends(get_db),current:SystemUser=Depends(get_current_user)) :
    old_student=student_repo.get_student_by_id(student,db=db)

    return old_student


@route.patch("/update/{student_id}",response_model=StudentOut)
def update_by_student_id(student_id:int,update_student_value:StudentUpdate,db:Session=Depends(get_db),current_user:SystemUser=Depends(get_current_user))->StudentOut:
    update_student=student_repo.update_student(student_id=student_id,update_student_value=update_student_value,db=db)
    return update_student

    
