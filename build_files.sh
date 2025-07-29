#!/bin/bash
# Build script for Django static files
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput
echo "Static files collected successfully!"
echo "Favicon file:"
ls -la staticfiles/favicon.ico 