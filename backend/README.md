# Getting started

1. Install [docker-compose](https://docs.docker.com/compose/install/)
2. Seed the database:
```
docker-compose run api python manage.py seed_db
```
3. Run the server:
```
docker-compose up
```

The backend will run at `http://localhost:5000`.

## Tests

Tests can be run with
```
docker-compose run api pytest
```
