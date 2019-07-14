FROM alpine

RUN apk update &&\
    apk add --no-cache \
    nginx \
    && mkdir /app

COPY . /app

WORKDIR /app

