# ChatGPT Image Organiser

A simple tool for downloading images from a ChatGPT conversation and organising them into a local folder.

---

## What it does

- Finds image URLs from the currently loaded ChatGPT conversation  
- Downloads those images through the browser  
- Moves downloaded images from your Downloads folder into a chosen folder  
- Avoids filename clashes by automatically renaming duplicates  

---

## How to use

### 1. Download images from ChatGPT

Open the ChatGPT conversation you want to collect images from.

Open Developer Tools:

```
F12 → Console
```

Paste the code from:

```
browser_script.js
```

Press Enter.

The images will download into your Downloads folder.

> Note: Scroll through the conversation first so older images are loaded on the page.

---

### 2. Organise the downloaded images

Open `main.py` and check the folder settings near the top:

```python
SOURCE_FOLDER = str(Path.home() / 'Downloads')
DEST_FOLDER = str(Path.home() / 'Pictures' / 'ChatGPT Images')
```

Then run:

```bash
python main.py
```

The script will move matching image files into your destination folder.

---

## Files

- `browser_script.js` — browser console script for downloading ChatGPT images  
- `main.py` — Python script for moving and organising downloaded images  
- `.gitignore` — ignores local Python environment/cache files  

---

## Current limitations

- Only works with images currently loaded in the browser  
- Requires pasting JavaScript into the browser console  
- ChatGPT page structure may change over time and require updates  

---

## Future improvements

- One-click browser extension  
- Duplicate detection by image content  
- Cleaner filename generation  
- Simple user interface  
- Automatic folder selection  

---

## Why I built this

I built this to make it easier to collect screenshots and uploaded images from long ChatGPT conversations without manually scrolling through chats and saving each image one by one.
