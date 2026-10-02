from fastapi import APIRouter, Depends
import schemas, models, database
from sqlalchemy.orm import Session
from typing import Annotated
from database import SessionLocal
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException, status

router = APIRouter(prefix="/login", tags=["login"])

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
# JWT settings
''' Enter the CMD comond 'openssl rand -hex 32', then get the secret key'''
SECRET_KEY = '54683b4bdb3e29e0edd8dc3f819653bf80e0f0bd11650ae46e1117e51d23df9d'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 10
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='login')

def get_db():
    db = SessionLocal()  
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


def generate_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

'''Login route to authenticate user'''
@router.post('/')
def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    seller = db.query(models.Seller).filter(models.Seller.username == request.username).first()
    if not seller:
        return {"error": "Invalid username..."}
    if not bcrypt_context.verify(request.password, seller.password):
        return {"error": "Invalid password..."}
    
    # Generate JWT token (If username and password is correct)
    '''Why we need JWT login: It allows us to protect our routes with time-limited tokens that automatically expire,
       providing secure, stateless authentication without storing session data on the server. '''
    
    ''' access_token will eg. aaaa.bbbb.cccc (three parts separated by dots)'''
    access_token = generate_token(data={"sub": seller.username})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credential_exception
    return token_data