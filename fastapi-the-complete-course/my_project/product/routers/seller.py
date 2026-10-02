from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated
import schemas
import models
from database import engine, SessionLocal
from typing import List
from passlib.context import CryptContext

router = APIRouter(
    prefix="/sellers",
    tags=["sellers"]
    )

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SessionLocal()  
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

'''here we create seller with hashed password'''
'''use the DisplayProduct schema 'response_model=schemas.DisplayProduct' to hide the price field'''
@router.post('/', response_model=schemas.DisplaySeller)
def create_seller(request: schemas.Seller, db: db_dependency):
    new_seller = models.Seller(
        username=request.username,
        email=request.email,
        password=bcrypt_context.hash(request.password)
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller

@router.get('/show_all_sellers')
def get_all_sellers(db: db_dependency):
    product = db.query(models.Seller).all()
    return product
