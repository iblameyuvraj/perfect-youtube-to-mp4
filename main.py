import os
import sys

# ==========================================
# 📁 CONFIGURATION: DOWNLOAD FOLDER SETUP
# Set your desired download folder path here.
# Default: 'downloads' folder in the script directory
# ==========================================
DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")

# Create folder if it does not exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
# ==========================================

try:
    import yt_dlp
except ImportError:
    print("\n❌ 'yt-dlp' library is not installed!")
    print("👉 Please run: pip install yt-dlp\n")
    sys.exit(1)


def progress_hook(d):
    """Hook to display real-time download progress"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', '').strip()
        eta = d.get('_eta_str', '').strip()
        sys.stdout.write(f"\r⏳ Downloading... {percent} | Speed: {speed} | ETA: {eta}  ")
        sys.stdout.flush()
    elif d['status'] == 'finished':
        print("\n✅ Download complete! Processing and saving file...")


def download_youtube_video(video_url: str):
    """Download YouTube video using yt-dlp"""
    if not video_url.strip():
        print("⚠️ URL cannot be empty!")
        return

    print(f"\n📂 Download Folder: {DOWNLOAD_DIR}")
    print("🔍 Fetching video information...\n")

    # yt-dlp configurations
    ydl_opts = {
        # Best mp4 video or best combined format
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        # File save template: Folder / Video Title.extension
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
        'quiet': False,
        'no_warnings': True,
        # YouTube client bypass for SABR / "The page needs to be reloaded" error
        'extractor_args': {
            'youtube': {
                'player_client': ['ios', 'android', 'mweb']
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            title = info.get('title', 'Video')
            filename = ydl.prepare_filename(info)
            print("\n" + "=" * 50)
            print("🎉 Success! Video downloaded successfully!")
            print(f"🎬 Title: {title}")
            print(f"📍 Saved at: {filename}")
            print("=" * 50 + "\n")
    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ Download Error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error occurred: {e}")


def main():
    print("=" * 50)
    print("   🎥 YOUTUBE VIDEO DOWNLOADER (Python / yt-dlp)   ")
    print("=" * 50)
    print(f"📁 Save directory: {DOWNLOAD_DIR}\n")

    while True:
        try:
            url = input("🔗 Enter YouTube video URL (or 'q' to quit): ").strip()
            
            if not url:
                continue

            if url.lower() in ['q', 'quit', 'exit']:
                print("\n👋 Goodbye!\n")
                break

            download_youtube_video(url)
            print("-" * 50)

        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Program terminated.")
            break


if __name__ == "__main__":
    main()
