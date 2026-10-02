from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name : str
    description : str
    price : int

'''Schema for displaying product details, I hide the 'price' field'''
class DisplayProduct(BaseModel):
    name:str
    description:str
    seller: 'DisplaySeller'
    class config:
        orm_mode = True


class Seller(BaseModel):
    username: str
    email: str
    password: str

class DisplaySeller(BaseModel):
    username: str
    email: str
    class config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

