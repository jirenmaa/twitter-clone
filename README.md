<p>
  <h1>Twitter Clone</h1>
  <p>Attempting to create a twitter clone project</p>
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

This is an experimental project that I choose to learn more about frontend and backend development and how they interact.

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

### Running locally with docker 🐳

```sh
$ git clone https://github.com/jirenmaa/twitter-clone.git
```

running the docker compose

```sh
$ docker-compose build && docker-compose up -d
```

If you are not configuring email, you must run the django container to receive emails for your user registration.

```sh
$ docker-compose run --rm service-backend
```

### Running locally with git clone

Assume you have 'python', 'node', 'docker' (optional), and'redis' (for email queue) installed to run the project.

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

After installing both dependencies, you must configure the '.env' file in order to run the project. After you've set up '.env,' you can now start redis and celery.

```sh
NOTE: You must leave the redis server running by not close the terminal.

$ redis-server
```

```sh
$ celery -A celeryapp.tasks worker -l info
```

Before you can run Django, you must first create a database in Postgresql. Or you can do this by running the following command:

```sh
$ createdb -U postgres twitter-clone
```

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
