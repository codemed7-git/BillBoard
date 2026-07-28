#!/usr/bin/env bash
set -o errexit

echo "Waiting for database and applying migrations..."
attempt=1
max_attempts=30
until python manage.py migrate --noinput; do
  if [ "$attempt" -ge "$max_attempts" ]; then
    echo "Migrations failed after ${max_attempts} attempts"
    exit 1
  fi
  echo "Database not ready, retry ${attempt}/${max_attempts}..."
  attempt=$((attempt + 1))
  sleep 2
done

echo "Creating rubrics and users..."
python manage.py create_initial_data

echo "Starting Gunicorn..."
exec gunicorn samplesite.wsgi:application --bind "0.0.0.0:${PORT:-8000}"
