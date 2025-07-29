#!/bin/bash
# Build script for Django static files
pip install -r requirements.txt
python manage.py collectstatic --noinput 