from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.student_schema import StudentCreate,StudentOut
from sqlalchemy.orm import Session
from model.student import Student  
from typing import List
from auth.auth_dependancy import get_current_user

def create_student(student:StudentCreate,db:Session)->StudentOut:
    old_student=db.query(Student).filter(Student.name==student.name and Student.birth==student.birth).first()

    if old_student:
        raise HTTPException(status_code=400,detail="Student name alredy exists")
    
    new_student=Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    new_student=StudentOut(stud_id=new_student.stud_id,
                           name=new_student.name,
                           course=new_student.course,
                           year=new_student.year,
                           contract=new_student.contract,
                           gender=new_student.gender,
                           birth=new_student.birth)
    

    return new_student