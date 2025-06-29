from passlib.context import CryptContext


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

#hashing the registered password
def hashpassword(password:str):
    return pwd_context.hash(password)


#verifing the password
def verifypassword(original_password:str,hashed_password:str) -> bool:
    return pwd_context.verify(original_password,hashed_password)