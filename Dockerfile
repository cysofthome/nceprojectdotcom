FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /app
ADD . /app
COPY requirements.txt /app/
RUN pip install pipenv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system

COPY . /app
