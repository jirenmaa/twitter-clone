FROM python:3.8-slim

WORKDIR /usr/src

COPY . /usr/src

RUN sed -i 's/\r$//g' /usr/src/compose/rest/entrypoint \
  && sed -i 's/\r$//g' /usr/src/compose/rest/runserver \
  && chmod +x /usr/src/compose/rest/entrypoint \
  && chmod +x /usr/src/compose/rest/runserver \
  # install required system dependencies
  && apt-get update && apt-get install --no-install-recommends -y \
  # psycopg2 dependencies
  libpq-dev gcc \
  # dependencies for git
  && apt-get install -y git \
  # install django depedencies
  && pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/usr/src/compose/rest/entrypoint"]
