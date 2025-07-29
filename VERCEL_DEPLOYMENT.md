# Vercel Deployment Checklist

## Pre-Deployment Checklist

### ✅ Code Changes Made

- [x] Updated `vercel.json` with proper static file routing
- [x] Updated `vercel_app.py` with better error handling
- [x] Updated `runtime.txt` to Python 3.11.9
- [x] Created `build_files.sh` for build process
- [x] Updated `.gitignore` to exclude Vercel files
- [x] Created `vercel_settings.py` for Vercel-specific settings
- [x] Updated `settings.py` with production defaults

### ✅ Files Ready for Deployment

- [x] `vercel.json` - Vercel configuration
- [x] `vercel_app.py` - WSGI application
- [x] `requirements.txt` - Python dependencies
- [x] `runtime.txt` - Python version
- [x] `build_files.sh` - Build script
- [x] All Django templates and static files

## Deployment Steps

### 1. Install Vercel CLI

```bash
npm i -g vercel
```

### 2. Deploy to Vercel

```bash
vercel
```

### 3. Set Environment Variables in Vercel Dashboard

Go to your Vercel project settings and add these environment variables:

#### Required Variables:

```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-vercel-domain.vercel.app
```

#### Email Configuration (for local testing):

```
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST_USER=manmeetsingh28603@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=manmeetsingh28603@gmail.com
ADMIN_EMAIL=manmeetsingh28603@gmail.com
```

### 4. Important Notes

#### Email Functionality:

- **Local Development**: Uses SMTP with Gmail
- **Vercel Production**: Uses console backend (emails logged to console)
- **For Production Email**: Consider using external email services like SendGrid

#### Database:

- **SQLite**: Resets on each deployment
- **For Persistent Data**: Consider using external databases like PostgreSQL

#### Static Files:

- Automatically served by Vercel
- No additional configuration needed

## Post-Deployment Verification

### ✅ Check These Items:

- [ ] Website loads correctly
- [ ] Contact form works (check console for email logs)
- [ ] Static files (CSS, images) load properly
- [ ] All pages render correctly
- [ ] No 500 errors in Vercel logs

### 🔧 Troubleshooting

#### If Contact Form Doesn't Work:

1. Check Vercel function logs
2. Verify environment variables are set
3. Check if CSRF token is being sent correctly

#### If Static Files Don't Load:

1. Verify `vercel.json` routing is correct
2. Check if files are in the correct directories
3. Ensure build process completed successfully

#### If Database Errors Occur:

1. Check if migrations ran successfully
2. Verify SQLite file permissions
3. Consider using external database for production

## Production Considerations

### Security:

- ✅ DEBUG=False in production
- ✅ Secret key is properly set
- ✅ Allowed hosts configured
- ✅ Security headers enabled

### Performance:

- ✅ Static files optimized
- ✅ WhiteNoise configured
- ✅ Caching enabled
- ✅ Gzip compression (handled by Vercel)

### Monitoring:

- ✅ Logging configured
- ✅ Health check endpoint available
- ✅ Error tracking ready

## Next Steps After Deployment

1. **Set up custom domain** (optional)
2. **Configure external email service** (recommended)
3. **Set up external database** (for persistent data)
4. **Configure monitoring and analytics**
5. **Set up CI/CD pipeline** (optional)

---

**Your Django portfolio is now ready for Vercel deployment! 🚀**
