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
    
    # Configure email backend for Vercel
    # Option 1: Gmail SMTP (requires App Password)
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = 'smtp.gmail.com'
    # EMAIL_PORT = 587
    # EMAIL_USE_TLS = True
    # EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'manmeetsingh28603@gmail.com')
    # EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')  # Use App Password from Gmail
    # DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    
    # Option 2: Resend (recommended - free up to 100 emails/day)
    # First install: pip install resend
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = 'smtp.resend.com'
    # EMAIL_PORT = 587
    # EMAIL_USE_TLS = True
    # EMAIL_HOST_USER = 'resend'
    # EMAIL_HOST_PASSWORD = os.environ.get('RESEND_API_KEY', '')
    # DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'manmeetsingh28603@gmail.com')
    
    # Gmail SMTP Configuration
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'manmeetsingh28603@gmail.com')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    
    # Debug email configuration
    print(f"Email configuration:")
    print(f"EMAIL_HOST_USER: {EMAIL_HOST_USER}")
    print(f"EMAIL_HOST_PASSWORD: {'*' * len(EMAIL_HOST_PASSWORD) if EMAIL_HOST_PASSWORD else 'NOT SET'}")
    print(f"EMAIL_BACKEND: {EMAIL_BACKEND}")
    
    # Fallback to console if no email credentials are set
    if not EMAIL_HOST_PASSWORD:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        print("Warning: No email credentials found. Using console backend.")
    else:
        print("Email credentials found. Using SMTP backend.")
    
    # Configure static files for Vercel
    # On Vercel, we need to use a different approach for static files
    STATIC_URL = '/static/'
    
    # Try to use /tmp directory for static files (writable on Vercel)
    import tempfile
    STATIC_ROOT = tempfile.gettempdir() + '/staticfiles'
    
    # Use WhiteNoise for static file serving
    STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'
    
    # Ensure static files are served even if collectstatic hasn't been run
    WHITENOISE_USE_FINDERS = True
    WHITENOISE_AUTOREFRESH = True
    
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