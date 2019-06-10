#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER safeboda_user;
    ALTER USER safeboda_user WITH SUPERUSER;
    ALTER USER safeboda_user WITH ENCRYPTED PASSWORD '8GShwQeSMVULP0z1NcE+19QfYcYWKi';
EOSQL
