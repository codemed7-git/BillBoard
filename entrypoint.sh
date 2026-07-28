#!/bin/sh
set -e

echo "Waiting for PostgreSQL..."
python << 'EOF'
import os
import sys
import time

import psycopg2

host = os.environ.get("DB_HOST", "localhost")
port = os.environ.get("DB_PORT", "5432")
dbname = os.environ.get("DB_NAME", "billboard_db")
user = os.environ.get("DB_USER", "postgres")
password = os.environ.get("DB_PASSWORD", "postgres")

for attempt in range(60):
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        conn.close()
        sys.exit(0)
    except psycopg2.OperationalError:
        if attempt == 59:
            print("PostgreSQL is not available after 60 seconds", file=sys.stderr)
            sys.exit(1)
        time.sleep(1)
EOF

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

if [ "${LOAD_INITIAL_DATA:-true}" = "true" ]; then
  echo "Loading initial data..."
  python manage.py create_initial_data
fi

echo "Starting application..."
exec "$@"
