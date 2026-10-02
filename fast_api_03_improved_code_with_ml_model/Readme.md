## Imsurance Premium API

1) Create venv
    - python3 -m venv venv
2) Activate venv
    - venv/scripts/activate (Linux)
    - source venv/bin/activate (Mac)

3) install requirements.txt
    - pip install -r requirements.txt

4) mentione the version of library
    - pip freeze > requirements.txt

5) Run the api
    - uvicorn app:app --reload

6) create dockerfile

7) Build the docker image
    - docker build -t rishabh013/insurance-premium-api .

8) Docker login
    - docker login

9) Upload docker file into dockerHUB
    - docker push rishabh013/insurance-premium-api

10) Then, Pull the dockerfile from the dockerhub and test in docker desktop
    - docker run -p 8000:8000 rishabh013/insurance-premium-api







