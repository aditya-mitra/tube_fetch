FROM python:3.8-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
RUN pip install pipenv

# deps for psycopg2
RUN apt-get update && apt-get -y install libpq-dev gcc

COPY ./Pipfile ./Pipfile.lock ./

RUN pipenv install --deploy --ignore-pipfile

COPY . .

# we can skip this if .env was already added with proper config with docker-compose
RUN cp .env.example .env