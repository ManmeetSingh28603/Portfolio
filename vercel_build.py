#!/usr/bin/env python
"""
Build script for Vercel deployment
This script runs before the application starts to collect static files
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    # Add the project directory to Python path
    project_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(project_dir))
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
    
    # Import Django
    import django
    django.setup()
    
    # Collect static files
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput', '--clear'])
    
    print("Static files collected successfully!")
    
    # Check if staticfiles directory exists and has content
    staticfiles_dir = project_dir / 'staticfiles'
    if staticfiles_dir.exists():
        print(f"Static files directory created at: {staticfiles_dir}")
        for item in staticfiles_dir.rglob('*'):
            if item.is_file():
                print(f"  - {item.relative_to(staticfiles_dir)}")
    else:
        print("Warning: staticfiles directory was not created!")

if __name__ == '__main__':
    main() 