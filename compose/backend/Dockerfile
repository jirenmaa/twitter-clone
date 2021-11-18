FROM python:3.8-slim

WORKDIR /usr/src/backend

COPY . /usr/src/backend

RUN sed -i 's/\r$//g' /usr/src/backend/compose/backend/entrypoint \
  && sed -i 's/\r$//g' /usr/src/backend/compose/backend/runserver \
  && chmod +x /usr/src/backend/compose/backend/entrypoint \
  && chmod +x /usr/src/backend/compose/backend/runserver \
  # install required system dependencies
  && apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev gcc \
  # dependencies for git
  && apt-get install -y git \
  # install django depedencies
  && pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/usr/src/backend/compose/backend/entrypoint"]
