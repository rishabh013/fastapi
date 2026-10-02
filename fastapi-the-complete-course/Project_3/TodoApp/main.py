from fastapi import FastAPI, Depends, HTTPException, Path
import models
from database import engine,SessionLocal
from routers import auth, todos, admin, users

app = FastAPI()

'''It is only run if the database tables are not created'''
models.Base.metadata.create_all(bind=engine)

## Adding auth router it will execute the code in auth.py, todos.py, admin.py, users.py file
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
