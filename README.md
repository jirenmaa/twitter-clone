<p>
  <h1>Twitter Clone</h1>
  <h2>work in progress 🚧</h2>
  <p>A Twitter clone project</p>
</p>

## Table Of Contents

- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Running project](#getting-started)
- [License](#license)
- [Authors](#authors)

## About The Project

this is an experimental project that I choose to learning more about frontend and backend and how they work together.

## Built With

|                       Django Rest Framework                        |                      Vue JS                       |                       Docker                        |
| :----------------------------------------------------------------: | :-----------------------------------------------: | :-------------------------------------------------: |
| ![https://www.django-rest-framework.org](git-images/icons8-django.png) | ![https://v3.vuejs.org](git-images/icons8-vue-js.png) | ![https://www.docker.com](git-images/icons8-docker.png) |

## Getting Started

Assume you've installed `python`, `node`, `docker` (optional), `redis` (for email queue) to run the project.

### Running locally with docker 🐳

clone the git repository

```sh
$ git clone https://github.com/jirenmaa/twitter-clone.git
```

running the docker compose file

```sh
$ docker-compose build && docker-compose up -d && docker run service-frontend
```

### Running locally with git clone

clone the git repository

```sh
$ git clone https://github.com/jirenmaa/twitter-clone.git
```

installing python depedencies

```sh
$ pip install -r requirements.txt
```

installing vue depedencies

```sh
$ cd website && yarn install
```

after installed the depdencies, you need to setup `.env` file for the project.

runing celery worker and redis

```sh
$ redis-server
```

```sh
$ celery -A celeryapp.tasks worker -l info
```

before running the server, you need to create the database first in `postgres` with name `twitter-clone`.

running the `web` and `rest` from root project.

```sh
$ yarn website
```

```sh
$ python3 manage.py runserver
```


## License

Distributed under the MIT License. See [LICENSE](https://github.com/jirenmaa/https://github.com/jirenmaa/twitter-clone/blob/main/LICENSE.md) for more information.

## Authors

- *Ahmad alwi* - [jirenmaa](https://github.com/jirenmaa/)
