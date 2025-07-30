from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
import logging
import os

logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    """Main portfolio page view with contact form"""
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            try:
                # Check if we're on Vercel (serverless environment)
                is_vercel = getattr(settings, 'IS_VERCEL', False) or 'VERCEL_ENV' in os.environ
                
                # Try to save to database first (for admin panel)
                try:
                    contact = contact_form.save()
                    send_contact_email(contact)
                except Exception as db_error:
                    logger.warning(f"Could not save to database: {db_error}")
                    # Fallback: send email without database
                    contact_data = contact_form.cleaned_data
                    # Add current date for email templates
                    from django.utils import timezone
                    contact_data['created_at'] = timezone.now()
                    send_contact_email_vercel(contact_data)
                
                # Check if it's an AJAX request
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Thank you! Your message has been sent successfully.'
                    })
                else:
                    messages.success(request, 'Thank you! Your message has been sent successfully.')
                    return redirect('portfolio:home')
                
            except Exception as e:
                logger.error(f"Error processing contact form: {e}")
                error_message = 'Sorry, there was an error sending your message. Please try again.'
                
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'status': 'error',
                        'message': error_message
                    }, status=500)
                else:
                    messages.error(request, error_message)
        else:
            error_message = 'Please correct the errors below.'
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                logger.error(f"Form validation errors: {contact_form.errors}")
                return JsonResponse({
                    'status': 'error',
                    'message': error_message,
                    'errors': contact_form.errors
                }, status=400)
            else:
                messages.error(request, error_message)
    
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'portfolio/home.html', context)

@require_http_methods(["GET"])
def health_check(request):
    """Health check endpoint for monitoring"""
    try:
        # Basic health check - you can add database checks here if needed
        return JsonResponse({
            'status': 'healthy',
            'service': 'portfolio',
            'version': '1.0.0'
        })
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return JsonResponse({
            'status': 'unhealthy',
            'error': str(e)
        }, status=500)

def send_contact_email(contact):
    """Send email notification for new contact form submission"""
    try:
        subject = f'New Contact Form Message from {contact.name}'
        
        # Email to admin
        admin_message = render_to_string('portfolio/email/contact_admin.html', {
            'contact': contact
        })
        
        # Create HTML email for admin
        admin_email = EmailMessage(
            subject=subject,
            body=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL],
        )
        admin_email.content_subtype = "html"
        admin_email.send()
        
        # Email to sender (confirmation)
        sender_message = render_to_string('portfolio/email/contact_confirmation.html', {
            'contact': contact
        })
        
        # Create HTML email for sender
        sender_email = EmailMessage(
            subject='Thank you for Reaching out to me!',
            body=sender_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[contact.email],
        )
        sender_email.content_subtype = "html"
        sender_email.send()
        
        logger.info(f"Contact email sent successfully for {contact.email}")
        
    except Exception as e:
        logger.error(f"Error sending contact email: {e}")
        raise

def send_contact_email_vercel(contact_data):
    """Send email notification for new contact form submission on Vercel (no database)"""
    try:
        # Debug email settings
        logger.info(f"Email settings - BACKEND: {settings.EMAIL_BACKEND}")
        logger.info(f"Email settings - HOST: {settings.EMAIL_HOST}")
        logger.info(f"Email settings - PORT: {settings.EMAIL_PORT}")
        logger.info(f"Email settings - USER: {settings.EMAIL_HOST_USER}")
        logger.info(f"Email settings - FROM: {settings.DEFAULT_FROM_EMAIL}")
        logger.info(f"Email settings - ADMIN: {settings.ADMIN_EMAIL}")
        
        subject = f'New Contact Form Message from {contact_data["name"]}'
        
        # Email to admin
        admin_message = render_to_string('portfolio/email/contact_admin.html', {
            'contact': contact_data
        })
        
        logger.info(f"Sending admin email to: {settings.ADMIN_EMAIL}")
        # Create HTML email for admin
        admin_email = EmailMessage(
            subject=subject,
            body=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.ADMIN_EMAIL],
        )
        admin_email.content_subtype = "html"
        admin_email.send()
        
        # Email to sender (confirmation)
        sender_message = render_to_string('portfolio/email/contact_confirmation.html', {
            'contact': contact_data
        })
        
        logger.info(f"Sending confirmation email to: {contact_data['email']}")
        # Create HTML email for sender
        sender_email = EmailMessage(
            subject='Thank you for contacting me!',
            body=sender_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[contact_data['email']],
        )
        sender_email.content_subtype = "html"
        sender_email.send()
        
        logger.info(f"Contact email sent successfully for {contact_data['email']} (Vercel)")
        
    except Exception as e:
        logger.error(f"Error sending contact email on Vercel: {e}")
        logger.error(f"Error details: {str(e)}")
        raise
