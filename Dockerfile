FROM python:3.7-slim-buster

RUN apt update -y && apt install -y build-essential libpq-dev

RUN pip install mlflow
RUN pip install psycopg2-binary --no-binary psycopg2-binary

# the second part of the Dockerfile
COPY entrypoint.sh entrypoint.sh
RUN chmod u+x entrypoint.sh

ENTRYPOINT [ "bash", "entrypoint.sh" ]