"""
Vercel-specific settings for Django portfolio

This file contains settings specifically for deploying on Vercel's serverless platform.
It overrides the main settings.py file to handle Vercel's environment constraints,
particularly around file system access and logging.
"""
import os
from .settings import *

# Vercel environment detection
IS_VERCEL = os.environ.get('VERCEL_ENV') is not None

# Set the IS_VERCEL flag in settings
IS_VERCEL = True

if IS_VERCEL:
    # Force debug to False on Vercel
    DEBUG = False
    
    # Add Vercel domain to allowed hosts
    VERCEL_DOMAIN = os.environ.get('VERCEL_URL', '')
    if VERCEL_DOMAIN:
        ALLOWED_HOSTS = list(ALLOWED_HOSTS) + [VERCEL_DOMAIN] if isinstance(ALLOWED_HOSTS, (list, tuple)) else [VERCEL_DOMAIN]
    
    # Use console email backend on Vercel (no SMTP)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
    # Disable file-based logging and use console logging instead
    # This prevents the FileNotFoundError on Vercel's serverless environment
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'loggers': {
            'django': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False,
            },
        },
    } 