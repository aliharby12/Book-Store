FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
RUN apk add zlib-dev jpeg-dev gcc musl-dev
COPY requirements.txt /code/
# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
# RUN apk add --no-cache jpeg-dev zlib-dev
RUN pip install -r requirements.txt
# RUN apk del .tmp
COPY . /code/

RUN adduser -D user
USER user