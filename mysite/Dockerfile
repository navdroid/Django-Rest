# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7.5

FROM python:3.7.5
ENV PYTHONUNBUFFERED 1
WORKDIR /code
ADD . /code/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
