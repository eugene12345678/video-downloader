# from pytube import YouTube

# # Set the headers to simulate a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "en-US,en;q=0.9",
# }

# # Update the YouTube request headers
# YouTube._default_headers = headers

# link = input("Enter the URL of the video you want to download: ")

# try:
#     yt = YouTube(link)  # Will use the custom headers
#     downloader = yt.streams.get_highest_resolution()
#     print("Downloading video...")
#     downloader.download(filename="video_downloader.mp4")
#     print("Video downloaded successfully!")
# except Exception as e:
#     print(f"An error occurred: {e}")

# import yt_dlp

# link = input("Enter the URL of the video you want to download: ")

# # Set the options for downloading the video with headers
# ydl_opts = {
#     "format": "137",  # You can specify the format ID here (e.g., 137 for 1080p MP4)
#     "outtmpl": "video_downloader.%(ext)s",
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Referer": link  # Add Referer header to mimic a real YouTube request
#     },
# }

# try:
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([link])
#     print("Video downloaded successfully!")
# except Exception as e:
#     print(f"An error occurred: {e}")

# import yt_dlp

# link = input("Enter the URL of the video you want to download: ")

# # Set the options for downloading the video with both video and audio
# ydl_opts = {
#     "format": "bestvideo+bestaudio/best",  # This will download the best available video and audio and merge them
#     "outtmpl": "video_downloader.%(ext)s",  # Set the output template to save the file with the appropriate extension
#     "merge_output_format": "mp4",  # Merge the video and audio into an MP4 file
#     "headers": {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "en-US,en;q=0.9",
#         "Referer": link  # Add Referer header to mimic a real YouTube request
#     },
# }

# try:
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([link])  
#     print("Video and audio downloaded successfully!")
# except Exception as e:
#     print(f"An error occurred: {e}")

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
