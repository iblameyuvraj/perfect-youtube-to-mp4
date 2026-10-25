# YouTube Video Downloader

A lightweight and robust YouTube video downloader built with Python and `yt-dlp`.

## 🚀 Setup & Run:

1. **Activate virtual environment:**
   ```bash
   source .venv/bin/activate
   ```
   *(Or install dependencies globally: `pip install -r requirements.txt`)*

2. **Run the script:**
   ```bash
   python3 main.py
   ```

3. **Enter YouTube URL:**
   Paste your YouTube video link when prompted in the terminal. Type `q` to exit.

## 📁 Customizing Download Folder
You can customize the destination folder path at the top of [main.py](file:///Users/yuvraj/Documents/yuvraj/youtube-to-mp4/main.py):
```python
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
```
