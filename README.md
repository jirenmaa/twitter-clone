<p>
  <h1>Twitter Clone</h1>
  <p>An attempt to create a twitter clone website (for learning purpose)</p>
</p>

![preview](git-assets/preview.gif)

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
| ![https://www.django-rest-framework.org](git-assets/icons8-django.png) | ![https://v3.vuejs.org](git-assets/icons8-vue-js.png) | ![https://www.docker.com](git-assets/icons8-docker.png) |

## Features

- [x] Authentication
- [x] User Profile (tweets, media, replies, liked tweets)
- [x] Create Tweet
- [x] Delete Tweet
- [x] Like, Unlike Tweet
- [x] Reply Tweet

## Getting Started

### Running locally with docker 🐳

```sh
$ git clone https://github.com/jirenmaa/twitter-clone.git
```

change and configure `.django.example` to `.django` and `.postgres.example` to `.postgres` in `.envs` folder, then running the docker compose

```sh
$ docker-compose build && docker-compose up
```

The site will be hosted on [http://localhost:8080](http://localhost:8080)

NOTE: if email settings in `.django` env is not configure, you will recive email for user activation (register) from console when you running `docker-compose up`.

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

Distributed under the MIT License. See [LICENSE](https://github.com/jirenmaa/twitter-clone/blob/master/LICENSE) for more information.

## Authors

- *Ahmad alwi* - [jirenmaa](https://github.com/jirenmaa/)
