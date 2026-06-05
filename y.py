import os
import threading
import customtkinter as ctk
from tkinter import filedialog
import yt_dlp

# ---------------- SETTINGS ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FFMPEG_PATH = r"C:\Users\Rajesh\Downloads\ffmpeg-2026-06-04-git-c27a3b12e3-essentials_build\ffmpeg-2026-06-04-git-c27a3b12e3-essentials_build\bin"

app = ctk.CTk()
app.geometry("800x600")
app.title("🎬 Advanced YouTube Downloader")

# ---------------- VARIABLES ---------------- #

folder_var = ctk.StringVar()
quality_var = ctk.StringVar(value="720p")
download_type = ctk.StringVar(value="Video")

# ---------------- FUNCTIONS ---------------- #

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def open_folder():
    folder = folder_var.get()
    if folder and os.path.exists(folder):
        os.startfile(folder)

def get_format():
    quality = quality_var.get()

    if quality == "360p":
        return "18"

    elif quality == "720p":
        return "136+140"

    elif quality == "1080p":
        return "137+140"

    return "18"

def download():

    url = url_entry.get().strip()
    folder = folder_var.get()

    if not url:
        status_label.configure(text="❌ Enter URL")
        return

    if not folder:
        status_label.configure(text="❌ Select Folder")
        return

    progress_bar.set(0)

    def progress_hook(d):

        if d["status"] == "downloading":

            percent = d.get("_percent_str", "0%")

            progress_label.configure(
                text=f"Downloading {percent}"
            )

            try:
                value = float(
                    percent.replace("%", "").strip()
                ) / 100

                progress_bar.set(value)

            except:
                pass

        elif d["status"] == "finished":
            progress_label.configure(
                text="🔄 Processing..."
            )

    def run():

        try:

            status_label.configure(
                text="⬇ Download Started..."
            )

            ydl_opts = {
                "ffmpeg_location": FFMPEG_PATH,
                "outtmpl": f"{folder}/%(title)s.%(ext)s",
                "ignoreerrors": True,
                "progress_hooks": [progress_hook],
                "merge_output_format": "mp4",
                "noplaylist": False,
                "writethumbnail": True
            }

            if download_type.get() == "Video":

                ydl_opts["format"] = get_format()

                ydl_opts["postprocessors"] = [{
                    "key": "FFmpegVideoRemuxer",
                    "preferedformat": "mp4"
                }]

            else:

                ydl_opts["format"] = "bestaudio/best"

                ydl_opts["postprocessors"] = [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192"
                }]

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            progress_bar.set(1)

            status_label.configure(
                text="✅ Download Complete"
            )

            progress_label.configure(
                text="🎉 Finished Successfully"
            )

        except Exception as e:

            status_label.configure(
                text=f"❌ {str(e)}"
            )

    threading.Thread(
        target=run,
        daemon=True
    ).start()

# ---------------- UI ---------------- #

title = ctk.CTkLabel(
    app,
    text="🎬 Advanced YouTube Downloader",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

url_entry = ctk.CTkEntry(
    app,
    width=650,
    placeholder_text="Paste YouTube Video or Playlist URL"
)
url_entry.pack(pady=10)

ctk.CTkButton(
    app,
    text="📁 Select Download Folder",
    command=select_folder,
    width=250
).pack(pady=10)

ctk.CTkLabel(
    app,
    textvariable=folder_var,
    wraplength=700
).pack()

ctk.CTkLabel(
    app,
    text="Download Type"
).pack(pady=(20, 5))

ctk.CTkOptionMenu(
    app,
    variable=download_type,
    values=["Video", "MP3"]
).pack()

ctk.CTkLabel(
    app,
    text="Quality"
).pack(pady=(20, 5))

ctk.CTkOptionMenu(
    app,
    variable=quality_var,
    values=["360p", "720p", "1080p"]
).pack()

ctk.CTkButton(
    app,
    text="⬇ Download",
    command=download,
    width=250,
    height=40
).pack(pady=20)

progress_bar = ctk.CTkProgressBar(
    app,
    width=600
)
progress_bar.pack()
progress_bar.set(0)

progress_label = ctk.CTkLabel(
    app,
    text="Waiting..."
)
progress_label.pack(pady=10)

status_label = ctk.CTkLabel(
    app,
    text=""
)
status_label.pack()

ctk.CTkButton(
    app,
    text="📂 Open Download Folder",
    command=open_folder,
    width=250
).pack(pady=20)

app.mainloop()