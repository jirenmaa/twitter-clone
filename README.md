<p>
  <h1>Twitter Clone</h1>
  <p>A Twitter clone project</p>
</p>

## Table Of Contents

- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Running project using docker](#getting-started)
  - [Running project locally](#getting-started)
- [License](#license)
- [Authors](#authors)

## About The Project

this is an experimental project that I choose to learning more about frontend and backend and how they work together.

## Built With

|                       Django Rest Framework                        |                      Vue JS                       |                       Docker                        |
| :----------------------------------------------------------------: | :-----------------------------------------------: | :-------------------------------------------------: |
| ![https://www.django-rest-framework.org](git-images/icons8-django.png) | ![https://v3.vuejs.org](git-images/icons8-vue-js.png) | ![https://www.docker.com](git-images/icons8-docker.png) |


## Features
- [x] Authentication
- [x] User Profile (tweets, media, replies, liked tweets)
- [x] Create Tweet
- [ ] Delete Tweet
- [x] Like, Unlike Tweet
- [x] Reply Tweet
- [ ] Follow, Unfollow User

## Getting Started

Assume you've installed `python`, `node`, `docker` (optional), `redis` (for email queue) to run the project.

### Running locally with docker 🐳

clone the git repository

```sh
$ git clone https://github.com/jirenmaa/twitter-clone.git
```

running the docker compose file

```sh
$ docker-compose build && docker-compose up -d
```

if you are not setting up for email configuration, u have to run the django container to recive the email

```sh
$ docker-compose run --rm service-backend
```

### Running locally with git clone

clone the git repository

```sh
$ git clone https://github.com/jirenmaa/twitter-clone.git
```

installing django & vue depedencies

```sh
$ pip install -r requirements.txt
```

```sh
$ cd website && yarn install
```

after installing both depdencies, you have to setup `.env` file to running the project.

after you have setting up `.env`, you now can running redis and celery.

```sh
NOTE: you have to let the redis server keep running and not closing the console

$ redis-server
```

```sh
$ celery -A celeryapp.tasks worker -l info
```

before you can run the django, you have to create database first in postgresql.

```sh
$ createdb -U username -O password twitter-clone
```

or you can create manually in `psql` console.

running the rest of the project

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
