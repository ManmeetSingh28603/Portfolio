# Deployment Guide

This guide will help you deploy your Django portfolio to various hosting platforms.

## Quick Deploy Options

### 1. Vercel (Recommended - Free & Easy)

**Steps:**

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import your GitHub repository
4. Set environment variables in Vercel dashboard:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your-app-name.vercel.app`
5. Deploy!

**Environment Variables in Vercel:**

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.vercel.app
```

### 2. Railway (Recommended - Free Tier)

**Steps:**

1. Push your code to GitHub
2. Go to [railway.app](https://railway.app)
3. Connect your GitHub repository
4. Set environment variables in Railway dashboard
5. Deploy automatically on push

**Environment Variables in Railway:**

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.railway.app
```

### 3. Heroku (Paid - Professional)

**Steps:**

1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```
4. Deploy: `git push heroku main`

## Environment Variables Setup

### For Local Development

Create a `.env` file in your project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### For Production

Set these environment variables in your hosting platform:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com,your-app-name.platform.com
```

## Generate a New Secret Key

If you need a new Django secret key, run:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Static Files

The project is configured to collect static files automatically. The `staticfiles/` directory contains all collected static files for production.

## Database

The project uses SQLite by default. For production, consider using PostgreSQL:

1. **Add PostgreSQL to requirements.txt:**

   ```
   psycopg2-binary==2.9.9
   ```

2. **Update DATABASES in settings.py:**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': config('DB_NAME'),
           'USER': config('DB_USER'),
           'PASSWORD': config('DB_PASSWORD'),
           'HOST': config('DB_HOST'),
           'PORT': config('DB_PORT', default='5432'),
       }
   }
   ```

## Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` (50+ characters)
- [ ] Proper `ALLOWED_HOSTS` configuration
- [ ] HTTPS enabled
- [ ] Static files collected and served
- [ ] Environment variables set
- [ ] Database properly configured

## Troubleshooting

### Common Issues

1. **Static files not loading**

   - Run: `python manage.py collectstatic --noinput`
   - Check `STATIC_ROOT` configuration

2. **500 Internal Server Error**

   - Check environment variables
   - Verify `ALLOWED_HOSTS` includes your domain
   - Check logs in hosting platform

3. **Database errors**
   - Ensure database is properly configured
   - Run migrations: `python manage.py migrate`

### Platform-Specific Issues

**Vercel:**

- Ensure `vercel.json` is in root directory
- Check build logs for errors

**Railway:**

- Verify environment variables are set
- Check deployment logs

**Heroku:**

- Ensure `Procfile` is in root directory
- Check build logs: `heroku logs --tail`

## Performance Optimization

1. **Enable caching** (if needed)
2. **Optimize images** in static files
3. **Use CDN** for static assets
4. **Enable compression** on hosting platform

## Monitoring

After deployment, monitor:

- Application logs
- Error rates
- Response times
- Resource usage

## Backup Strategy

1. **Database backups** (if using external database)
2. **Code repository** (GitHub)
3. **Environment variables** (documented securely)
4. **Static files** (version controlled)

## SSL/HTTPS

Most modern hosting platforms provide SSL certificates automatically. Ensure:

- HTTPS redirects are enabled
- Mixed content warnings are resolved
- Security headers are properly configured
