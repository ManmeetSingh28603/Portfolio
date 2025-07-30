import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.vercel_settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

# Get the WSGI application
application = get_wsgi_application()

# For Vercel - always serve static files
application = StaticFilesHandler(application)

# For Vercel
app = application 