# This project will be switching our focus to TODOS instead of BOOKS.
# New information will incude
    - Full SQL Database
    - Authentication (JWT), usename and password
    - Authorization
    - Hashing passwords
# Creating a Todo Table
    - We will create new Todo Table Models for our application
    - we will be using these tools to save records throughout this project
        - Webpage
        - FastAPI
        - Database

1) Create a databas.py file
    - mention the databse url, engine, session alls

2) create a models.py
    - mention the class in which define the structured of table which we have to create

3) Run the main.py file
    - uvicorn main:app --reload
    - todos.db automatic created

OR

3) Go to console on same directory and use the sqlite3 for inserting the data
    - sqlite3 todos.db
    - .tables (check the all tables avialability)
    - .schema (check the schema of the tables)
    - Insert the data:
        - insert into todos (title, description, priority, complete) values ('Test element', 'he is getting hungry', 3, False);

### Authentication and Authorization

# Encrypted hashed password
pip isntall passlib
pip install bcrypt==4.0.1

# JWT dependenct
pip install "python-jose[cryptograpgy]"




