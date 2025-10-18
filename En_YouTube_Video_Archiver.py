import PySimpleGUI as sg
import re
from pytube import YouTube
import urllib.request
import os

sg.theme('Dark')

layout = [
    [sg.Text('Enter the YouTube video link:'), sg.InputText()],
    [sg.Button('Download'), sg.Button('Cancel')]
]

window = sg.Window('YouTube Video Archiver', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if re.search(r'\byoutube.com\b', values[0]) or re.search(r'\byoutu.be\b', values[0]):
        video = YouTube(values[0])
        title = video.title
        output_path = os.path.join(os.environ['UserProfile'], 'Desktop', title)

        # Create folder if not exists
        os.makedirs(output_path, exist_ok=True)

        # Download the video
        video.streams.get_highest_resolution().download(output_path)

        # Save video info
        info_path = os.path.join(output_path, "info.txt")
        with open(info_path, "w", encoding="utf-8") as text:
            text.write("Video description:\n" + video.description + "\n\n")
            text.write("Views:\n" + str(video.views) + "\n\n")
            text.write("Publish date:\n" + str(video.publish_date))

        # Download thumbnail
        thumbnail_path = os.path.join(output_path, "THUMBNAIL.jpg")
        urllib.request.urlretrieve(video.thumbnail_url, thumbnail_path)

        sg.popup('Video downloaded successfully:', video.title)
    else:
        sg.popup('Invalid link, please try again.')

window.close()