# URL Copier Chrome Extension

A simple Chrome extension that allows you to copy the current tab's URL to your clipboard with a single click.

## Features

- One-click URL copying
- Clean and modern user interface
- Visual feedback when URL is copied
- Displays the current URL in the popup
- Lightweight and fast

## Installation

### Option 1: Load as Unpacked Extension (Development)

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable "Developer mode" by toggling the switch in the top right corner
3. Click "Load unpacked"
4. Select the `chrome-extension` directory from this project
5. The extension should now appear in your extensions list

### Option 2: Create Icons (Optional)

The extension includes a Python script to create custom icons:

```bash
# Install Pillow (if not already installed)
pip install Pillow

# Run the icon creation script
cd chrome-extension
python3 create_icons.py
```

If you don't create custom icons, Chrome will use default placeholder icons, and the extension will still work perfectly.

## Usage

1. Click the extension icon in your Chrome toolbar
2. A popup will appear showing the current tab's URL
3. Click the "Copy Current URL" button
4. The URL will be copied to your clipboard
5. A success message will appear confirming the copy

## Files

- `manifest.json` - Extension configuration and metadata
- `popup.html` - The popup interface HTML
- `popup.js` - JavaScript for handling URL copying
- `popup.css` - Styling for the popup interface
- `create_icons.py` - Optional script to generate extension icons
- `README.md` - This file

## Permissions

This extension requires the following permissions:

- `activeTab` - To access the URL of the current active tab
- `clipboardWrite` - To copy the URL to the clipboard

## Customization

You can customize the extension by modifying:

- **Colors**: Edit the gradient in `popup.css` (currently purple/blue gradient)
- **Button style**: Modify the `#copyBtn` styles in `popup.css`
- **Extension name**: Change the `name` field in `manifest.json`

## Browser Compatibility

This extension uses Manifest V3 and is compatible with:

- Google Chrome (version 88+)
- Microsoft Edge (Chromium-based)
- Other Chromium-based browsers that support Manifest V3

## License

This extension is part of the nanochat project. See the main project LICENSE file for details.

## Troubleshooting

**Extension doesn't load:**
- Make sure Developer mode is enabled in `chrome://extensions/`
- Check the console for any error messages

**Copy button doesn't work:**
- Ensure the extension has the necessary permissions
- Check if clipboard access is allowed in your browser settings

**Icons not showing:**
- Run the `create_icons.py` script to generate icons
- Or create your own 16x16, 48x48, and 128x128 PNG files named `icon16.png`, `icon48.png`, and `icon128.png`
