FROM python:3.9-slim-buster

RUN apt update -y && apt install -y build-essential libpq-dev

RUN pip install -U pip
RUN pip install mlflow==2.4.0
RUN pip install psycopg2-binary --no-binary psycopg2-binary
RUN pip install -U sqlparse SQLAlchemy

# the second part of the Dockerfile
COPY entrypoint.sh entrypoint.sh
RUN chmod u+x entrypoint.sh

ENTRYPOINT [ "bash", "entrypoint.sh" ]
