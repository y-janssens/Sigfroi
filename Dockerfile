# syntax=docker/dockerfile:1
FROM python:3.10 AS build
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#RUN python manage.py collectstatic --noinput --clear

COPY . .