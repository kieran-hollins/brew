# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /python-docker

COPY ./requirements.txt /python-docker
RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP=__init__.py

CMD ["gunicorn", "brew:create_app"]
RUN ["python3", "flask", "--app", "brew init db"]


EXPOSE 8000