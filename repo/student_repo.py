from fastapi import APIRouter,Depends,HTTPException,status
from database.database import get_db
from schema.student_schema import StudentCreate,StudentOut,GetStudentID,StudentUpdate
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


def get_student_by_id(student:int,db:Session):

    old_student=db.query(Student).filter(Student.stud_id==student).first()

    if old_student is None:
        raise HTTPException(status_code=404,detail=f"Student id {student} is not found")
    
    new_student=StudentOut(stud_id=old_student.stud_id,
                           name=old_student.name,
                           course=old_student.course,
                           year=old_student.year,
                           contract=old_student.contract,
                           gender=old_student.gender,
                           birth=old_student.birth)
    

    return new_student

def update_student(student_id,update_student_value:StudentUpdate,db:Session)->StudentOut:
    old_student=db.query(Student).filter(Student.stud_id==student_id).first()

    if old_student is None:
        raise HTTPException(status_code=404,detail=f"Student id {student_id} is not found")
    
    update_data = update_student_value.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(old_student, key, value)

    db.commit()
    db.refresh(old_student)

    update_student=StudentOut(stud_id=old_student.stud_id,
                              name=old_student.name,
                              course=old_student.course,
                              year=old_student.year,
                              contract=old_student.contract,
                              birth=old_student.birth,
                              gender=old_student.gender)
    return update_student



