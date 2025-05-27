from pydantic import BaseModel
from typing import Optional
from schema.enum import Status
from datetime import datetime


class PublisherBase(BaseModel):
    publisher_name:str

class PublisherCreate(PublisherBase):
    pass

class PublisherOut(PublisherBase):
    publisher_id:int

    class Config:
        orm_mode=True
class PublisherUpdate(BaseModel):
    publisher_name:Optional[str]=None


