from pydantic import BaseModel
from schema.enum import Gender
from typing import Optional
from datetime import date,datetime


class StudentBase(BaseModel):
    name:str
    course:str
    year:int
    contract:str
    birth:date
    gender:Gender


class StudentCreate(StudentBase):
    pass


class StudentOut(StudentBase):
    stud_id:int

    class Config:
        orm_mode=True


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    course: Optional[str] = None
    year: Optional[int] = None
    contract: Optional[str] = None
    birth: Optional[date] = None
    gender: Optional[Gender] = None



class GetStudentID(BaseModel):
    student_id:int




    
