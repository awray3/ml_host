FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY ./app /app/app

COPY ./requirements ./requirements

RUN pip install -r requirements/server.txt