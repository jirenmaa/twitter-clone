FROM python:3.8-slim

WORKDIR /usr/src/celery-worker

COPY . /usr/src/celery-worker

# install required system dependencies
RUN  apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for git
  && apt-get install -y git \
  # install django depedencies
  && pip install --no-cache-dir -r requirements.txt
