## 1) Run the fast api file 
-----------
uvicorn main:app --reload

OR

uvicorn main:app --host 0.0.0.0 --port 9000 --reload   # use this for any specific port
-----------

## 2) Create pipeline to run local host (EC2 machine to local)
----------
ssh -N rishabh@10.101.40.38 -L 8857:localhost:9000
----------