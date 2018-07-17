FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /sandbox/gistandard
WORKDIR /sandbox/gistandard
ADD . /sandbox/gistandard
RUN apt-get update && apt-get -y install nginx
RUN pip install uwsgi && pip install -r requirements
