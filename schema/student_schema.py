from pydantic import BaseModel
from schema.enum import Gender
from typing import Optional
from datetime import date


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
    name:Optional[str]
    course:Optional[str]
    year:Optional[int]
    contract:Optional[str]
    birth:Optional[date]
    gender:Optional[Gender]



