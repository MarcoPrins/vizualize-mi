# Getting started

1. Install [docker-compose](https://docs.docker.com/compose/install/) and build the container with:
```
docker-compose build
```
2. Seed the database:
```
docker-compose run api python manage.py seed_db
```
3. Add file called .env in this directory with the following contents:
```
FLASK_APP=wsgi.py
FLASK_ENV=development
```

4. Run the server:
```
docker-compose up
```

The backend will run at `http://localhost:5000`.

## Tests

Tests can be run with
```
docker-compose run api pytest
```
