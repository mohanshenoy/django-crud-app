FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN pip install Django==3.2.6
RUN pip install psycopg2

# RUN django-admin startproject ContactApp 

#COPY . /code/
CMD python manage.py runserver 0.0.0.0:8000
