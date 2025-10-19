import PySimpleGUI as sg
import re
from pytube import YouTube,Channel,Playlist
import urllib.request
import os
sg.theme('Dark')

layout = [
            [sg.Text('Enter the YouTube video link:'), sg.InputText()],
            [sg.Button('Download'), sg.Button('Cancel')]]

window = sg.Window('YouTube Video Archiver', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  
        break
    if re.search(r'\byoutube.com\b', values[0]) or re.search(r'\byoutu.be\b', values[0]):
        video = YouTube(values[0])
        title = video.title
        output_path=f"{os.environ['UserProfile']}/Desktop/{title}"
        YouTube(values[0]).streams.get_highest_resolution().download(output_path)
        path=f"{os.environ['UserProfile']}/Desktop/{title}/info.txt"
        text = open(path, "w", encoding="utf-8")
        text.write("Video description: "+'\n'+video.description+'\n')
        izleyici = str(video.views)
        text.write("Views: "+'\n'+izleyici+'\n')
        tarih = str(video.publish_date)
        text.write("Publish date: "+'\n'+tarih)
        text.close()
        url = video.thumbnail_url
        jpg=f"{os.environ['UserProfile']}/Desktop/{title}/THUMBNAIL.jpg"
        urllib.request.urlretrieve(url,jpg)
        sg.popup('Video downloaded successfully: ', video.title)
    else:
        sg.popup('Invalid link, please try again.... ')
window.close()
