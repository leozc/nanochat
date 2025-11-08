#!/usr/bin/env python3
"""
Create simple placeholder PNG icons without external dependencies.
Uses base64-encoded minimal PNG data.
"""

import base64

# Minimal valid PNG files (solid color squares)
# These are tiny but valid PNG files that Chrome will accept

# 16x16 purple icon
icon16_data = base64.b64decode(
    b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAE0lEQVQ4jWNgYGD4T0FgHFUw'
    b'MgAA+eMH/YAiLvgAAAAASUVORK5CYII='
)

# 48x48 purple icon
icon48_data = base64.b64decode(
    b'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAGUlEQVRoge3BAQ0AAADCoPdP'
    b'bQ43oAAAAAAAvg0hAAAB0RKkWwAAAABJRU5ErkJggg=='
)

# 128x128 purple icon
icon128_data = base64.b64decode(
    b'iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAAHElEQVR4nO3BAQ0AAADCoPdP'
    b'bQ8HFAAAAAAA4N8AKvgAAUXRw1wAAAAASUVORK5CYII='
)

def create_icons():
    try:
        with open('icon16.png', 'wb') as f:
            f.write(icon16_data)
        print("Created icon16.png")

        with open('icon48.png', 'wb') as f:
            f.write(icon48_data)
        print("Created icon48.png")

        with open('icon128.png', 'wb') as f:
            f.write(icon128_data)
        print("Created icon128.png")

        print("\nPlaceholder icons created successfully!")
        print("These are minimal placeholder images. For better icons, consider:")
        print("1. Using the create_icons.py script with Pillow installed")
        print("2. Creating custom icons with an image editor")
        print("3. Using an online icon generator")

    except Exception as e:
        print(f"Error creating icons: {e}")

if __name__ == '__main__':
    create_icons()
