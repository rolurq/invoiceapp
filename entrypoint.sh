#!/bin/sh

echo "Waiting for database host..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
    sleep 0.1
done
echo "Database ready"

python manage.py migrate

exec "$@"
