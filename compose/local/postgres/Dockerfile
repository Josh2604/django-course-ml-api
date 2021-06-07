FROM postgres:10.17-alpine
RUN mkdir -p /tmp/psql_data/
COPY compose/local/postgres/structure.sql /docker-entrypoint-initdb.d/