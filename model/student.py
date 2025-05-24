from sqlalchemy import create_engine, Column, Integer, String,Numeric,Enum,ForeignKey,DateTime
from schema.enum import Gender
from database.database import Base


class Student(Base):
    __tablename__="student"

    stud_id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    course=Column(String)
    year=Column(Integer)
    contract=Column(String)
    birth=Column(DateTime)
    gender=Column(Enum(Gender))
    