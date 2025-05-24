from pydantic import BaseModel,EmailStr,constr
from typing import Optional
from schema.enum import UserRole


class StaffBase(BaseModel):
    name:str
    contract:str
    email:EmailStr
    address:str
    role:UserRole


class StaffCreate(StaffBase):
     password: constr(min_length=6)

class StaffOut(StaffBase):
    staff_id:int

    class Config:
        orm_mode=True


class StaffUpdate(BaseModel):
    name:Optional[str]
    contract:Optional[str]
    email:Optional[EmailStr]
    address:Optional[str]
    role:Optional[UserRole]
    password:Optional[constr(min_length=6)]

