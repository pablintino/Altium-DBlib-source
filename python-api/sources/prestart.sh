#! /usr/bin/env bash

# Let the DB start
sleep 1;

if [ -n "$APP_MIGRATIONS_ENABLED" ]; then
    # Run migrations
    echo "Running migrations scripts"
    flask db upgrade -d /app/migrations/
fi



