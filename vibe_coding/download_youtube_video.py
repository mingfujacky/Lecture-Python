from pytubefix import YouTube
from pathlib import Path

def download_youtube_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download(output_path = output_path)
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_dir = Path.cwd() / 'restricted' / 'assets' / 'video'
    download_dir.mkdir(parents=True, exist_ok=True)
    url = input("Please input the URL: ")
    download_youtube_video(url, download_dir)