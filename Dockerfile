# syntax=docker/dockerfile:1
FROM python:3.10 AS build
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM node:18.4-alpine AS builder
ENV NOVE_ENV production

WORKDIR /code/timeline/templates/timeline/front

COPY --from=build /code/timeline/templates/timeline/front/package-*.json .

RUN npm install

COPY . .

#RUN npm run build