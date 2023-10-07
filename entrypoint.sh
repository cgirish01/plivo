#!/bin/sh

# Wait for the database to be ready
while ! nc -z db 5432; do
    echo "Waiting for PostgreSQL..."
    sleep 1
done

echo "PostgreSQL started"

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the application using gunicorn
gunicorn messageService.wsgi:application --bind 0.0.0.0:8000
