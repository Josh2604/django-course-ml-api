# Django api and clean architecture

## Important paths
## .envs/
Includes local configurations for postgresql `host`,`port`,`db`,`user`,`password`.
```
.local/
    .prostgresql
```
## compose/
includes local and production Docker files and configurations

---
SQL script, allow to create some tables with default data and test in local environments 
```
compose/local/postgres/structure.sql
```
## requirements
This directory includes local and production dependencies

**local.txt: modify if you need dev dependencies**

**production: modify if you need production dependencies**

## users/tests/
* Unit and functional test
* benchmark example that allows you compare algorithms efficiency `benchmark_append_user.py` commands:
```
kernprof -l test.py
python -m line_profiler test.py.lprof
```

## Load test
Obtain metrics about your endpoints, `note: information depends by infrastructure that you are running`
```
locust --host=http://localhost:8000
```
---
## Run dev environment
```shell
    docker-compose -f local.yml up
```

## Run tests
```
    python manage.py test
```
**Note: If you want running this command in local environment you must run:**
```
    docker exec -it image_id /bin/sh
```
Inside the container run:
```
    python manage.py test
```
---
# Endpoints
POST /api/v1/users/ -> create new user
request:
```
{
    "name": "test",
    "apells": "test",
    "age": 10
}
```
response:
```
```

GET /api/v1/users/all -> get all users available

response:
```
```

GET /api/v1/users/:uid -> get a single user

response:
```
```

PUT /api/v1/users/:uid -> update a user registered

response:
```
```

DELETE /api/v1/users/:uid -> delete a user registered

response:
```
```

