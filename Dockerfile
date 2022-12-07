FROM python:3.12.0a1 AS build

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install --upgrade pip \
    && pip install -r requirements.txt


RUN python manage.py collectstatic --noinput --clear

COPY . .
