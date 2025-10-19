import customtkinter as ctk
from pytube import YouTube
import urllib.request
import os
import re

# App setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("YouTube Video Archiver")
app.geometry("400x200")

# Label
label = ctk.CTkLabel(app, text="Lütfen video linki giriniz:")
label.pack(pady=10)

# Input
url_entry = ctk.CTkEntry(app, width=300)
url_entry.pack(pady=5)

def download_video():
    url = url_entry.get()
    if re.search(r'\byoutube.com\b', url) or re.search(r'\byoutu.be\b', url):
        try:
            video = YouTube(url)
            title = video.title
            output_path = os.path.join(os.path.expanduser("~"), "Desktop", title)
            os.makedirs(output_path, exist_ok=True)

            # Download video
            video.streams.get_highest_resolution().download(output_path)

            # Save info
            info_path = os.path.join(output_path, "info.txt")
            with open(info_path, "w", encoding="utf-8") as f:
                f.write(f"Baþlýk: {title}\n")
                f.write(f"Açýklama:\n{video.description}\n")
                f.write(f"Görüntülenme: {video.views}\n")
                f.write(f"Yayýn Tarihi: {video.publish_date}\n")

            # Thumbnail
            thumb_path = os.path.join(output_path, "thumbnail.jpg")
            urllib.request.urlretrieve(video.thumbnail_url, thumb_path)

            ctk.CTkMessagebox(title="Success", message=f"Downloaded: {title}")
        except Exception as e:
            ctk.CTkMessagebox(title="Hata", message=str(e))
    else:
        ctk.CTkMessagebox(title="Bozuk Link", message="Lütfen geçerli bir YouTube Linki giriniz.")

def exit_app():
    app.destroy()

# Buttons
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=20)

download_btn = ctk.CTkButton(btn_frame, text="Ýndir", command=download_video)
download_btn.grid(row=0, column=0, padx=10)

cancel_btn = ctk.CTkButton(btn_frame, text="Ýptal", command=exit_app)
cancel_btn.grid(row=0, column=1, padx=10)

app.mainloop()