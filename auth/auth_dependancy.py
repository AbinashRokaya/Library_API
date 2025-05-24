from typing import Union,Any
from datetime import datetime
from auth.jwt import SECRET_KEY,ALGORITHM

from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
import jwt
from pydantic import ValidationError

from schema.token_shema import TokenPayload,SystemUser
from database.database import get_db
from model.staff import Staff
from datetime import datetime

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/auth/login')

async def get_current_user(token:str=Depends(oauth2_scheme))->SystemUser:
    try:
        payload=jwt.decode(token,SECRET_KEY,ALGORITHM)
        token_data=TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp)<datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate":"Bearer"},
            )
    except (jwt.PyJWTError,ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentails",
            headers={"www-Authenticate":"Bearer"},

        )
    user=token_data.sub

    if user is None:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
    )

    return SystemUser(username=user)
            
        
