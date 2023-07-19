# Todo application

## Setup

The first thing to do is to clone the repository:

```sh
$ cd Django_4-2
```

Create a virtual environment name `env` to install dependencies in and activate it:

```sh
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Create Environment file `.env` from `.env.example`
```sh
$ cp .env.example .env
```
Now add values in .env file

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.