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

# Run build script to collect static files if they don't exist
staticfiles_dir = project_dir / 'staticfiles'
if not staticfiles_dir.exists():
    try:
        # Import and run the build script
        from vercel_build import main as build_main
        build_main()
    except Exception as e:
        print(f"Warning: Could not collect static files: {e}")

application = get_wsgi_application()

# For Vercel
app = application 