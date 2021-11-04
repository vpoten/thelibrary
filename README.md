# TheLibrary

## Abstract

This service provides a REST API for basic library management.

## Technological stack

The stack used to create this API is:
* python
* flask
* flask-smorest
* sqlite
* pytest

## Docker execution of the app

#### Build image
```
docker build . -t thelibrary:latest
```

#### Run tests
```
docker run thelibrary:latest pytest tests/
```

#### Run server; bind to port 5000
```
docker run -p 5000:5000 thelibrary:latest
```

## Non docker execution of the project

Run the `install_local.sh` script from project root folder. This script will create the virtual environment with
all the required dependencies installed on it:
```bash
./scripts/install_local.sh
```

Activate the virtual environment:
```bash
. venv/bin/activate
```

Initialize the DB and run the flask app:

```bash
export FLASK_APP=src
flask init-db
flask run
```
**Note that DB initialization is only mandatory for the first time**.\
By default, the `flask run` command launches the app listening on port 5000.

Run the tests:
```bash
pytest -v
```

## API Swagger interface

It is possible to work with the API via Swagger UI from the url:
```
http://<host>:<port>/apidocs/swagger#/
```

Normally:

[http://127.0.0.1:5000/apidocs/swagger#/](http://127.0.0.1:5000/apidocs/swagger#/)

