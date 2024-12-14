import os
from yt_dlp import YoutubeDL

def download_video(url, output_path):
    try:
        url = url.strip()
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        options = {
            'format': 'bestvideo+bestaudio/best',  
            'merge_output_format': 'mp4',  
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }

        with YoutubeDL(options) as ydl:
            ydl.download([url])

        print("Download completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    save_path = input("Enter the directory to save the video (default is current directory): ").strip()

    if not save_path:
        save_path = os.getcwd()

    download_video(video_url, save_path)
