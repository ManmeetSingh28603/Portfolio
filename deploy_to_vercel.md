# Deploy to Vercel - Step by Step Guide

## After Pushing to GitHub

### 1. Go to Vercel

- Visit [vercel.com](https://vercel.com)
- Sign up/Login with your GitHub account

### 2. Import Your Repository

- Click "New Project"
- Select "Import Git Repository"
- Choose your portfolio repository
- Click "Import"

### 3. Configure Project Settings

- **Framework Preset**: Other
- **Root Directory**: `./` (leave as default)
- **Build Command**: Leave empty (Vercel will auto-detect)
- **Output Directory**: Leave empty
- **Install Command**: `pip install -r requirements.txt`

### 4. Set Environment Variables

Click "Environment Variables" and add:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.vercel.app
```

**Important**: Replace `your-secret-key-here` with the actual secret key from your `.env` file.

### 5. Deploy

- Click "Deploy"
- Wait for build to complete (usually 2-3 minutes)

### 6. Access Your Site

- Your site will be available at: `https://your-app-name.vercel.app`
- You can also set up a custom domain later

## Troubleshooting

### If Build Fails:

1. Check build logs in Vercel dashboard
2. Ensure all environment variables are set
3. Verify `requirements.txt` is in root directory
4. Check that `vercel.json` is properly configured

### If Site Shows 500 Error:

1. Check environment variables are correct
2. Verify `ALLOWED_HOSTS` includes your Vercel domain
3. Check Vercel function logs

### Common Issues:

- **Static files not loading**: Vercel handles this automatically
- **Database errors**: SQLite works fine on Vercel for portfolios
- **Environment variables**: Make sure they're set in Vercel dashboard

## Post-Deployment

### 1. Test Your Site

- Visit your Vercel URL
- Test all sections and links
- Check mobile responsiveness
- Verify contact form (if functional)

### 2. Set Up Custom Domain (Optional)

- Go to Vercel dashboard
- Click on your project
- Go to "Settings" → "Domains"
- Add your custom domain

### 3. Monitor Performance

- Check Vercel analytics
- Monitor build times
- Watch for any errors

## Environment Variables Reference

Make sure these are set in Vercel:

```env
SECRET_KEY=your-actual-secret-key-from-env-file
DEBUG=False
ALLOWED_HOSTS=your-app-name.vercel.app
```

## Success Checklist

- [ ] Code pushed to GitHub
- [ ] Repository imported to Vercel
- [ ] Environment variables set
- [ ] Build successful
- [ ] Site accessible
- [ ] All sections working
- [ ] Mobile responsive
- [ ] Links functional

Your portfolio should now be live on Vercel! 🚀
