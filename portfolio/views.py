from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from pathlib import Path

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def favicon(request):
    """Serve favicon directly"""
    favicon_path = Path(settings.BASE_DIR) / 'portfolio' / 'static' / 'images' / 'favicon.ico'
    if favicon_path.exists():
        return FileResponse(open(favicon_path, 'rb'), content_type='image/x-icon')
    else:
        # Fallback to staticfiles directory
        favicon_path = Path(settings.STATIC_ROOT) / 'images' / 'favicon.ico'
        if favicon_path.exists():
            return FileResponse(open(favicon_path, 'rb'), content_type='image/x-icon')
        else:
            from django.http import Http404
            raise Http404("Favicon not found")
