FROM postgres:10.7
RUN mkdir -p /docker-entrypoint-initdb.d
COPY docker-entrypoint-initdb.d/init-user-db.sh /docker-entrypoint-initdb.d/
RUN chmod -R 777 /docker-entrypoint-initdb.d
# COPY postgresql-check.sh /postgresql-check.sh
