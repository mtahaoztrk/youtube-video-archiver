# youtube-video-archiver
🎥 YouTube Video Archiver

A simple Python GUI application that allows you to download YouTube videos, along with their description, publish date, view count, and thumbnail image.
All files are automatically organized into a folder on your desktop named after the video title.

🧩 Features

Download any public YouTube video in the highest available resolution

Automatically save:

Video description

View count

Publish date

Thumbnail image

Simple and clean GUI using PySimpleGUI

Works on Windows (tested)

🖥️ How to Use

Run the application (youtube_video_archiver.py or .exe version).

Paste a valid YouTube link in the input box.

Click Download.

Wait until the popup message confirms that the video has been downloaded.

You’ll find a folder on your desktop with:

The video file

info.txt (description, views, date)

THUMBNAIL.jpg

⚙️ Requirements (for Python version)
pip install pytube PySimpleGUI

📦 Example Output Folder
Desktop/
 └── Example Video Title/
     ├── Example Video Title.mp4
     ├── info.txt
     └── THUMBNAIL.jpg

🧑‍💻 Author

Created by Muhammed Taha Öztürk
If you like this project, feel free to ⭐ star it on GitHub!
