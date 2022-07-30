# syntax=docker/dockerfile:1
FROM python:3.9
FROM node:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
