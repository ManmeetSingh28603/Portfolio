from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def home(request):
    """Main portfolio page view with contact form"""
    contact_form = ContactForm()
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            try:
                # Save the contact message
                contact = contact_form.save()
                
                # Send email notification
                send_contact_email(contact)
                
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
                logger.error(f"Error saving contact form: {e}")
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
        
        send_mail(
            subject=subject,
            message=admin_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        
        # Email to sender (confirmation)
        sender_message = render_to_string('portfolio/email/contact_confirmation.html', {
            'contact': contact
        })
        
        send_mail(
            subject='Thank you for contacting me!',
            message=sender_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact.email],
            fail_silently=False,
        )
        
        logger.info(f"Contact email sent successfully for {contact.email}")
        
    except Exception as e:
        logger.error(f"Error sending contact email: {e}")
        raise
