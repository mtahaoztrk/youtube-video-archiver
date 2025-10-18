import PySimpleGUI as sg
import re
from pytube import YouTube,Channel,Playlist
import urllib.request
import os
sg.theme('Dark')

layout = [
            [sg.Text('Video linki giriniz'), sg.InputText()],
            [sg.Button('indir'), sg.Button('iptal')]]

window = sg.Window('Youtube Video Stoklayici', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  
        break
    if re.search(r'\byoutube.com\b', values[0]) or re.search(r'\byoutu.be\b', values[0]):
        video = YouTube(values[0])
        title = video.title
        output_path=f"{os.environ['UserProfile']}/Desktop/{title}"
        YouTube(values[0]).streams.get_highest_resolution().download(output_path)
        path=f"{os.environ['UserProfile']}/Desktop/{title}/text.txt"
        text = open(path, "w", encoding="utf-8")
        text.write("Video aciklamasi: "+'\n'+video.description+'\n')
        izleyici = str(video.views)
        text.write("izlenme sayisi: "+'\n'+izleyici+'\n')
        tarih = str(video.publish_date)
        text.write("Video tarihi: "+'\n'+tarih)
        text.close()
        url = video.thumbnail_url
        jpg=f"{os.environ['UserProfile']}/Desktop/{title}/KAPAK.jpg"
        urllib.request.urlretrieve(url,jpg)
        sg.popup('Video indirildi: ', video.title)
    else:
        sg.popup('Link bulunamadi, tekrar deneyiniz... ')
window.close()
