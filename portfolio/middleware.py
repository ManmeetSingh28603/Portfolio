import os
from django.conf import settings
from django.http import FileResponse, Http404
from django.utils.deprecation import MiddlewareMixin
from pathlib import Path

class StaticFilesMiddleware(MiddlewareMixin):
    """
    Simple middleware to serve static files directly.
    This is a fallback for Vercel deployment.
    """
    
    def process_request(self, request):
        # Only handle static file requests
        if not request.path.startswith('/static/'):
            return None
            
        # Remove /static/ prefix
        static_path = request.path[8:]  # Remove '/static/' (8 characters)
        
        # Try to find the file in STATICFILES_DIRS
        for static_dir in settings.STATICFILES_DIRS:
            file_path = Path(static_dir) / static_path
            if file_path.exists() and file_path.is_file():
                try:
                    return FileResponse(open(file_path, 'rb'))
                except Exception:
                    continue
        
        # If not found in STATICFILES_DIRS, try STATIC_ROOT
        if hasattr(settings, 'STATIC_ROOT') and settings.STATIC_ROOT:
            file_path = Path(settings.STATIC_ROOT) / static_path
            if file_path.exists() and file_path.is_file():
                try:
                    return FileResponse(open(file_path, 'rb'))
                except Exception:
                    pass
        
        # File not found
        raise Http404(f"Static file '{static_path}' not found") 