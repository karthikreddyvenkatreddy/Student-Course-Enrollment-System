from datetime import datetime,timedelta,timezone
from typing import Optional
import jwt
import bcrypt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES =240

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password:str)-> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hased_password:str)->bool:
    return pwd_context.verify(plain_password,hased_password)

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm = ALGORITHM)

def get_current_user(token:str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return {"email":email}
    except :
        raise credentials_exception

