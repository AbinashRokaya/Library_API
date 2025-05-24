from fastapi import FastAPI,status,Depends,HTTPException,APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from schema.token_shema import Token
from auth.hashing import verifying_password,get_password_hashed
from database.database import get_db
from sqlalchemy.orm import Session
from model.staff import Staff
from auth.jwt import create_access_token

route=APIRouter(
    prefix=("/auth"),
    tags=['login']
)


@route.post("/login",response_model=Token)
def login(db:Session=Depends(get_db),form_data:OAuth2PasswordRequestForm=Depends()):
    get_user=db.query(Staff).filter(Staff.name==form_data.username).first()
    if not get_user:
        raise HTTPException(status_code=400,detail="Incorrect username")
    
    if not verifying_password(form_data.password,get_user.password):
        raise HTTPException(status_code=400,detail="Incorrect password")
    
    access_token=create_access_token(get_user.name)

    return {"access_token":access_token,"token_type":"bearer"}

