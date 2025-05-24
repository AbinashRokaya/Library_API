from sqlalchemy import String,Integer,Column,Enum
from database.database import Base
from schema.enum import UserRole

class Staff(Base):
    __tablename__="staff"

    staff_id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    contract=Column(String)
    email=Column(String)
    address=Column(String)
    password=Column(String)
    role=Column(Enum(UserRole),default=UserRole.assistant)
