import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).resolve().parent
sys.path.insert(0, str(project_dir))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Collect static files if they don't exist (for Vercel deployment)
staticfiles_dir = project_dir / 'staticfiles'
if not staticfiles_dir.exists():
    try:
        # Set environment to production for static file collection
        os.environ['DEBUG'] = 'False'
        
        # Import Django and collect static files
        import django
        django.setup()
        
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])
        
        print("Static files collected successfully!")
    except Exception as e:
        print(f"Warning: Could not collect static files: {e}")

application = get_wsgi_application()

# For Vercel
app = application 