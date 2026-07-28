#!/usr/bin/env bash
set -o errexit

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Loading initial data..."
python manage.py create_initial_data

echo "Starting Gunicorn..."
exec gunicorn samplesite.wsgi:application --bind "0.0.0.0:${PORT:-8000}"
