## Getting Started

# FastAPI-MySql

This contents the approach for FastAPI with MySQL

# Python Environment Setup :

python3 -m venv env
source env/bin/activate

pip install poetry

[https://python-poetry.org/]

### Install dependencies from requirements.txt

pip install -r requirements.txt

### Prereqs

- python 3.9+
- poetry

# Show tree of all packages

poetry show --tree

### Running the project first time

```console
$ poetry install
$ poetry run alembic upgrade head
$ run.bat
```

### Running the project after the first time

```console
$ run.bat
```

#### In macOS or Linux

```console
$ sh run.sh
```

## API Documentation

### Endpoints

#### GET /

#### GET /api/v1/users

#### GET /api/v1/users/{user_id}
