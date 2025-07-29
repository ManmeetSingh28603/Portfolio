# Logo and Favicon Setup

## Current Setup

- `final.png` - Your Memoji character image
- Used as both favicon and logo throughout the website

## To Replace with Your Actual Memoji Image

### Option 1: Replace the PNG (Recommended)

1. Save your Memoji image as `final.png` in this directory
2. Make sure it's a square image (64x64 pixels or larger)
3. The image will automatically be used as favicon and logo

### Option 2: Use Different Format

1. Save your Memoji image as `final.jpg` or another format in this directory
2. Update the template files to reference the new image:
   - In `portfolio/templates/portfolio/home.html`
   - Replace `{% static 'images/final.png' %}` with `{% static 'images/final.jpg' %}`

### Option 3: Multiple Formats for Better Compatibility

1. Save your Memoji image in multiple formats:
   - `favicon.ico` (16x16, 32x32, 48x48 pixels)
   - `final.png` (64x64 pixels)
   - `final.svg` (vector format)
2. Update the favicon links in the template:
   ```html
   <link
     rel="icon"
     type="image/x-icon"
     href="{% static 'images/favicon.ico' %}"
   />
   <link rel="icon" type="image/png" href="{% static 'images/final.png' %}" />
   <link rel="apple-touch-icon" href="{% static 'images/final.png' %}" />
   ```

## Image Specifications

- **Favicon**: 16x16, 32x32, or 64x64 pixels
- **Logo**: 64x64 pixels or larger (will be scaled down)
- **Format**: PNG (recommended), SVG, or ICO
- **Background**: Transparent or solid color that matches your theme

## Current Usage

The logo appears in:

1. Browser tab favicon
2. Navigation bar (next to "My Portfolio" text)
3. Footer (next to "My Portfolio" text)

## Testing

After replacing the image:

1. Clear your browser cache
2. Refresh the page
3. Check that the favicon appears in the browser tab
4. Verify the logo appears in the navigation and footer
