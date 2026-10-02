from fastapi import FastAPI
import models
from database import engine, SessionLocal
from routers import product, seller, login

app = FastAPI(
    title="Product Management API",
    description="API for managing products and sellers",
    version="2.0.0",
    terms_of_service="http://www.google.com",
    contact={
        "name": "Rishabh Developer",
        "email": "rishabhvishwakarma013@gmail.com"}
)

'''It is only run if the database tables are not created'''
models.Base.metadata.create_all(bind=engine)

app.include_router(product.router)
app.include_router(seller.router)
app.include_router(login.router)



