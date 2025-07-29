"""
Vercel-specific settings for Django portfolio
"""
import os
from .settings import *

# Vercel environment detection
IS_VERCEL = os.environ.get('VERCEL_ENV') is not None

if IS_VERCEL:
    # Force debug to False on Vercel
    DEBUG = False
    
    # Add Vercel domain to allowed hosts
    VERCEL_DOMAIN = os.environ.get('VERCEL_URL', '')
    if VERCEL_DOMAIN:
        ALLOWED_HOSTS = list(ALLOWED_HOSTS) + [VERCEL_DOMAIN] if isinstance(ALLOWED_HOSTS, (list, tuple)) else [VERCEL_DOMAIN]
    
    # Use console email backend on Vercel (no SMTP)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
    # Disable file logging on Vercel
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    } 