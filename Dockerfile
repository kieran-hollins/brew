# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "brew:create_app"]

EXPOSE 8000