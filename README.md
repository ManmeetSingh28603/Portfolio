# Manmeet Singh - Portfolio Website

A modern, responsive portfolio website built with Django and Tailwind CSS, optimized for production deployment on Vercel.

## Features

- 🎨 Modern, responsive design with Tailwind CSS
- 🌙 Dark/Light mode toggle
- 📱 Mobile-first responsive design
- ⚡ Fast loading with optimized static files
- 🔗 Interactive project cards with external links
- 📄 Resume download functionality
- 📧 Contact form
- 🚀 Production-ready deployment configuration
- 🔒 Security headers and best practices
- 📊 Comprehensive logging
- 🗄️ SQLite database (Vercel compatible)

## Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: Tailwind CSS (via CDN)
- **Database**: SQLite (Vercel compatible)
- **Server**: Gunicorn
- **Deployment**: Vercel (primary), Heroku, Railway ready

## Quick Start

### Local Development Setup

#### Prerequisites

- Python 3.11+
- pip

#### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd portfoliomy
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   # Create .env file with your settings
   echo SECRET_KEY=your-secret-key-here > .env
   echo DEBUG=True >> .env
   echo ALLOWED_HOSTS=localhost,127.0.0.1 >> .env
   ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Collect static files**

   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Visit the website**
   Open http://127.0.0.1:8000 in your browser

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here-change-this-in-production
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# Email Configuration (SMTP)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
ADMIN_EMAIL=manmeetsingh28603@gmail.com

# CORS Settings (optional)
CORS_ALLOWED_ORIGINS=https://your-domain.com,https://www.your-domain.com
```

### Setting up Gmail SMTP:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password:**
   - Go to [Google Account settings](https://myaccount.google.com/)
   - Security → 2-Step Verification → App passwords
   - Select "Mail" and generate a password
   - Use this password in `EMAIL_HOST_PASSWORD`
3. **Update your .env file** with your actual Gmail credentials
4. **Test the configuration** with: `python test_email.py`

## Production Deployment

### Vercel Deployment (Recommended)

1. **Install Vercel CLI**

   ```bash
   npm i -g vercel
   ```

2. **Deploy**

   ```bash
   vercel
   ```

3. **Set environment variables in Vercel dashboard**

   - Go to your project settings in Vercel
   - Add environment variables:
     - `SECRET_KEY`: Your Django secret key
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: Your Vercel domain
     - `EMAIL_BACKEND`: `django.core.mail.backends.console.EmailBackend`
     - `EMAIL_HOST_USER`: Your Gmail address
     - `EMAIL_HOST_PASSWORD`: Your Gmail app password
     - `DEFAULT_FROM_EMAIL`: Your Gmail address
     - `ADMIN_EMAIL`: Your email address

4. **Important Vercel Notes:**
   - Email functionality uses console backend on Vercel (no SMTP)
   - Static files are automatically served
   - Database is SQLite (resets on each deployment)
   - For persistent data, consider using external database

### Heroku Deployment

1. **Install Heroku CLI**

   ```bash
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Heroku app**

   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables**

   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

### Railway Deployment

1. **Connect your GitHub repository to Railway**
2. **Set environment variables in Railway dashboard**
3. **Deploy automatically on push**

## Security Features

- Environment variable management
- Production security headers
- CSRF protection
- XSS protection
- HSTS headers
- Secure cookie settings
- Content Security Policy (CSP)
- CORS configuration
- Session security
- Comprehensive logging

## Performance Optimizations

- Static file collection and serving with WhiteNoise
- CDN for Tailwind CSS
- Optimized images
- Minimal JavaScript
- Efficient CSS with Tailwind
- Database optimization
- Caching configuration

## Project Structure

```
portfoliomy/
├── myportfolio/          # Django project settings
├── portfolio/            # Main portfolio app
│   ├── templates/        # HTML templates
│   ├── static/          # Static files (CSS, JS, images)
│   └── views.py         # View functions
├── logs/                # Application logs
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel configuration
├── Procfile            # Heroku configuration
└── runtime.txt         # Python version specification
```

## Customization

### Adding New Projects

1. Edit `portfolio/templates/portfolio/sections/projects.html`
2. Add new project cards following the existing structure
3. Update project details, links, and technologies

### Updating Personal Information

1. Edit `portfolio/templates/portfolio/sections/hero.html` for main info
2. Edit `portfolio/templates/portfolio/sections/about.html` for skills
3. Edit `portfolio/templates/portfolio/sections/contact.html` for contact details

### Changing Colors/Theme

1. Edit `portfolio/templates/portfolio/base.html` for Tailwind configuration
2. Update color classes in template files
3. Modify dark/light mode colors as needed

## Monitoring and Logging

- Application logs are stored in `logs/django.log`
- Health check endpoint available at `/health/`
- Comprehensive error logging
- Performance monitoring ready

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- **Email**: manmeetsingh28603@gmail.com
- **LinkedIn**: [Manmeet Singh](https://www.linkedin.com/in/manmeet-singh-985834150/)
- **GitHub**: [ManmeetSingh28603](https://github.com/ManmeetSingh28603)
- **Instagram**: [_manmeet_singh_28_](https://www.instagram.com/_manmeet_singh_28_/)
