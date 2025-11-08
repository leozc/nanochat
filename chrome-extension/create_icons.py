#!/usr/bin/env python3
"""
Simple script to create placeholder icons for the Chrome extension.
"""

try:
    from PIL import Image, ImageDraw

    def create_icon(size, filename):
        # Create a new image with transparent background
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Draw a circle with the extension's color
        color = (102, 126, 234, 255)  # #667eea
        margin = 2
        draw.ellipse([margin, margin, size-margin, size-margin], fill=color)

        # Draw a smaller white circle in the center for a link/chain look
        center = size // 2
        inner_radius = size // 4
        draw.ellipse([center-inner_radius, center-inner_radius,
                     center+inner_radius, center+inner_radius],
                     fill=(255, 255, 255, 255))

        # Save the image
        img.save(filename)
        print(f"Created {filename}")

    # Create all three icon sizes
    create_icon(16, 'icon16.png')
    create_icon(48, 'icon48.png')
    create_icon(128, 'icon128.png')

    print("All icons created successfully!")

except ImportError:
    print("PIL/Pillow is not installed.")
    print("You can install it with: pip install Pillow")
    print("Or create your own icons manually (16x16, 48x48, 128x128 PNG files)")
