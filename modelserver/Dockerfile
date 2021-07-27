# Flask model server
# FROM python:3.7-alpine as base

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN mkdir /modelserver 
# WORKDIR /modelserver
# COPY ./requirements.txt /modelserver/requirements.txt

# RUN apk add --no-cache --virtual .build-deps \
#     g++ gcc python3-dev libffi-dev \
#     openssl-dev libxslt-dev musl-dev cargo

# RUN mkdir /venvs \
#     && pip install --upgrade pip \
#     && pip install --upgrade pip setuptools \
#     && pip install -r requirements.txt

# COPY . .

FROM python:3.6-stretch as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /modelserver 
WORKDIR /modelserver
COPY ./requirements.txt /modelserver/requirements.txt

RUN mkdir /venvs \
    && pip install --upgrade pip \
    && pip install --upgrade pip setuptools \
    && pip install -r requirements.txt

COPY . .
