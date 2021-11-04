# TheLibrary

## Abstract

This service provides a REST API for basic library management.

A [Swagger UI](#api-swagger-interface) is provided as documentation and working platform.


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

**Note: for the sake of simplicity an embedded sqlite database is used, no data will persist between container reboots**

## Non docker execution of the app

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


## API endpoints


### Authors

#### GET /api/authors

List authors

#### POST /api/authors

Add a new author

#### GET /api/authors/{author_id}

Get author by id

#### PUT /api/authors/{author_id}

Update an author

#### DELETE /api/authors/{author_id}

Delete an author

#### GET /api/authors/{author_id}/books

Get the books associated with a given author


### Categories

#### GET /api/categories

List categories

#### POST /api/categories

Add a new category

#### GET /api/categories/{category_id}

Get category by id

#### PUT /api/categories/{category_id}

Update a category

#### DELETE /api/categories/{category_id}

Delete a category

#### GET /api/categories/{category_id}/books

Get the books associated with a given category


### Books

#### GET /api/books

List books

#### POST /api/books

Add a new book

#### GET /api/books/{isbn}

Get book by id

#### PUT /api/books/{isbn}

Update a book

#### DELETE /api/books/{isbn}

Delete a book

#### GET /api/books/{isbn}/categories

Get book categories

#### POST /api/books/{isbn}/categories/{category_id}

Associate category to book

#### DELETE /api/books/{isbn}/categories/{category_id}

Disassociate category to book

#### GET /api/books/{isbn}/authors

Get book authors

#### POST /api/books/{isbn}/authors/{author_id}

Associate author to book

#### DELETE /api/books/{isbn}/authors/{author_id}

Disassociate author to book
