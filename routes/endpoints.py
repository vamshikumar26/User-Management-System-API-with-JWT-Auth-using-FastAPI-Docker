from fastapi import APIRouter,status,HTTPException,Depends
from schema.database import db
import json
from bson import ObjectId
from models.user_model import register
from hashing import hashpassword
from Oauth2 import get_current_user
from routes.passwordcheck import is_strong_password
router=APIRouter()

class JSONEncoder(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,ObjectId):
            return str(o)
        return super().default(o)
    
collection=db.users


#check whether database is connected
@router.get("/root",tags=["Database connection"])
def connection(get_current_user:register=Depends(get_current_user)):
    return "connected to mongo"

#user registration
@router.post("/register/",tags=["Login-Register"])
def registering(user:register,get_current_user:register=Depends(get_current_user)):
    existing=collection.find_one({"username":user.username})
    if existing :
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="user already exists")
    
    if not is_strong_password(user.password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="Password must be at least 8 characters long, include uppercase, lowercase, number, and special character.")
    user_dict=user.dict()
    user_dict["password"]=hashpassword(user.password)
    result=collection.insert_one(user_dict)
    if result:
        return {"message":"registered successfully"}
    return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)



#fetching user by name
@router.post("/fetch-only-one-user/{username}",tags=["operations"])
def fetching(username,get_current_user:register=Depends(get_current_user)):
    result=collection.find_one({"username":username})
    if result:
        return json.loads(JSONEncoder().encode(result))
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")

#fetching all the users
@router.get("/get-all-users/",tags=["fetching all user details"])
def fetch_users(get_current_user:register=Depends(get_current_user)):
    result=list(collection.find())
    return json.loads(JSONEncoder().encode(result))

#user-updation-details
@router.put("/details-updation/{username}",tags=["operations"])
def updation(username:str, user:register,get_current_user:register=Depends(get_current_user)):
    if not collection.find_one({"username":username}):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    result=collection.update_one({"username":username},{"$set":user.dict()})
    if "password" in result:
        result["password"]=hashpassword(result["password"])
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=" user not found")
    
    return "updated successfully"
    
#user-deletion
@router.delete("/delete-user/",tags=["operations"])
def deletinguser(username:str,get_current_user:register=Depends(get_current_user)):
    result = collection.delete_one({"username":username})
    if result:
        return "user deleted successfully"
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")

    