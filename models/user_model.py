from pydantic import BaseModel,Field
from typing import Optional,List

#Register
class register(BaseModel):
    username:str
    phone_number:str
    password:str=Field(...,examples=["****"])
    age:Optional[int]=None
    subjects:List[str]=None

#Login    
class Login(BaseModel):
    username:str
    password:str
  
#Accesss_Token  
class token(BaseModel):
    access_token:str
    token_type:str

#
class TokenData(BaseModel):
    username:Optional[str] = None 
        