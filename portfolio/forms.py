from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-gray-50 dark:bg-slate-700 border border-gray-300 dark:border-slate-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 transition-all duration-300 hover:bg-gray-100 dark:hover:bg-slate-600',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 bg-gray-50 dark:bg-slate-700 border border-gray-300 dark:border-slate-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 transition-all duration-300 hover:bg-gray-100 dark:hover:bg-slate-600',
                'placeholder': 'your.email@example.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-gray-50 dark:bg-slate-700 border border-gray-300 dark:border-slate-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 transition-all duration-300 hover:bg-gray-100 dark:hover:bg-slate-600',
                'rows': '4',
                'placeholder': 'Your message here...'
            })
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Name is required.")
        name = name.strip()
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        email = email.strip().lower()
        
        # Basic email format validation
        if '@' not in email or '.' not in email:
            raise forms.ValidationError("Please enter a valid email address.")
        
        # Check for common email format issues
        if email.count('@') > 1:
            raise forms.ValidationError("Email address cannot contain multiple @ symbols.")
        
        if email.startswith('@') or email.endswith('@'):
            raise forms.ValidationError("Please enter a valid email address.")
        
        if email.startswith('.') or email.endswith('.'):
            raise forms.ValidationError("Please enter a valid email address.")
        
        return email
    
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("Message is required.")
        message = message.strip()
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long. Please provide more details.")
        if len(message) > 2000:
            raise forms.ValidationError("Message is too long. Please keep it under 2000 characters.")
        return message 