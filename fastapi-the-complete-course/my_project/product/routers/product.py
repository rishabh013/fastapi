from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, models
from typing import Annotated
from database import SessionLocal
from typing import List
from .login import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["products"]
    )

def get_db():
    db = SessionLocal()  
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post('/')
def add(request: schemas.Product, db: db_dependency, current_user: Annotated[schemas.Seller, Depends(get_current_user)]):
    new_product = models.Product(
        name=request.name,
        description=request.description,
        price=request.price,
        seller_id=1
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get('/show_all_products')
def get_all_product(db: db_dependency, current_user: Annotated[schemas.Seller, Depends(get_current_user)]):
    product = db.query(models.Product).all()
    return product

'''use the DisplayProduct schema to hide the price field'''
@router.get('/', response_model = List[schemas.DisplayProduct])
def get_product(db: db_dependency):
    product = db.query(models.Product).all()
    return product

'''use the DisplayProduct schema to hide the price field'''
@router.get('/{id}', response_model=schemas.DisplayProduct)
def get_product_by_id(id: int, db: db_dependency):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    return product

@router.delete('/{id}')
def delete_product(id: int, db: db_dependency):
    db.query(models.Product).filter(models.Product.id == id).delete()
    db.commit()
    return 'Deleted'

@router.put('/{id}')
def update_product(id: int, request: schemas.Product, db: db_dependency):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        return 'Not Found'
    product.name = request.name
    product.description = request.description
    product.price = request.price
    db.commit()
    return 'Updated'
