from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer
import jwt_token_module

#Token url 
oauth2_scheme= OAuth2PasswordBearer(tokenUrl="login")

#fetching the current user details
def get_current_user(token:str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return jwt_token_module.verify_token(token,credentials_exception)