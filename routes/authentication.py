from fastapi import APIRouter,HTTPException,Depends,status
from fastapi.security import OAuth2PasswordRequestForm
from schema.database import db
from jwt_token_module import create_access_token
from hashing import verifypassword
from models.user_model import register
from Oauth2 import get_current_user

 
router = APIRouter()


#creating new collection for "authentication"
mycollection=db.authentication
collection = db.users

# Storing the login details for authentication
@router.post("/login/",tags=["Login-Register"],)
def login(request: OAuth2PasswordRequestForm = Depends()):
    user = collection.find_one({"username": request.username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    if not verifypassword(request.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )
    access_token = create_access_token(data={"sub": request.username})
    return {"access_token": access_token, "token_type": "bearer","message":"user logged in successfully"}