from pydantic import BaseModel
from typing import Optional

class TokenPayload(BaseModel):
    sub:str
    exp:int

class SystemUser(BaseModel):
    username:str
    
    
class Token(BaseModel):
    access_token:str
    token_type:str