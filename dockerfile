FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY ./app /app/app

COPY ./server_requirements.txt ./requirements.txt

RUN pip install -r requirements.txt