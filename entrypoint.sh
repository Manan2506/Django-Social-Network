#!/bin/sh

# Apply database migrations
python manage.py migrate

# Create superuser if not exists
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass') if not User.objects.filter(username='admin').exists() else None;" | python manage.py shell

# Start server
python manage.py runserver 0.0.0.0:8000
