# YouTube Video Downloader

A powerful Python-based YouTube video downloader that bypasses restrictions and allows downloading videos directly from YouTube with audio and video merged seamlessly. The downloader supports handling various YouTube parameters and saving videos in your desired directory.

---

## Features
- **Bypass YouTube Restrictions**: Downloads videos even with parameterized links.
- **High-Quality Downloads**: Fetches the best available video and audio quality.
- **Audio-Video Merge**: Ensures audio and video are combined into a single file.
- **Custom Output Directory**: Save videos in any directory of your choice.
- **User-Friendly**: Simple to use with minimal setup.

---

## Requirements
- Python 3.9 or higher
- `yt-dlp`: A modern YouTube video downloader library
- `os`: Standard Python library for file handling

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/eugene12345678/video-downloader.git
   cd video-downloader
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   > Ensure `yt-dlp` is installed by running:
   ```bash
   pip install yt-dlp
   ```

3. **Run the Script**
   ```bash
   python video_downloader.py
   ```

---

## Usage

1. **Provide the YouTube Video URL**
   - The downloader accepts parameterized YouTube links such as:
     ```
     https://youtu.be/dQw4w9WgXcQ?si=UNcLbv6nEybSHvSO
     ```

2. **Specify the Save Location**
   - Leave blank to save in the current directory.

### Example
```bash
python video_downloader.py
Enter the YouTube video URL: https://youtu.be/dQw4w9WgXcQ?si=UNcLbv6nEybSHvSO
Enter the directory to save the video (default is current directory): 
```

---

## Code Highlights

- **Automatic Handling of Parameters**: Strips and processes parameterized YouTube URLs effortlessly.
- **Audio and Video Merging**: Ensures smooth playback by merging streams using `yt-dlp`'s robust features.
- **Custom Output Directory**: Dynamically creates output directories if they don't exist.

---

## Troubleshooting

1. **Invalid URL Error**: Ensure the URL is a valid YouTube video link.
2. **Missing Dependencies**: Run the following to ensure all libraries are up-to-date:
   ```bash
   pip install --upgrade yt-dlp
   ```
3. **Python Version Warning**: Update Python to version 3.9 or higher:
   ```bash
   sudo apt update && sudo apt install python3.9
   ```

---

## Contributions

Feel free to fork this repository and submit pull requests. Contributions to improve functionality or add features are always welcome!

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Disclaimer

This tool is intended for personal use only. Respect copyright laws and YouTube's terms of service when downloading videos.
