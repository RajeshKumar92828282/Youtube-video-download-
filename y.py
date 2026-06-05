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
app.title("YouTube Downloader Pro")

folder_var = ctk.StringVar()
quality_var = ctk.StringVar(value="720p")

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
    q = quality_var.get()

    if q == "360p":
        return "18"
    elif q == "720p":
        return "136+140"
    elif q == "1080p":
        return "137+140"

    return "bestvideo+bestaudio/best"

def download_video():

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
                text=f"⬇ Downloading {percent}"
            )

            try:
                value = float(percent.replace("%", "").strip()) / 100
                progress_bar.set(value)
            except:
                pass

        elif d["status"] == "finished":
            progress_label.configure(
                text="🔄 Merging Audio + Video..."
            )

    def run():

        try:

            status_label.configure(
                text="🚀 Download Started"
            )

            ydl_opts = {
                "format": get_format(),
                "merge_output_format": "mp4",
                "ffmpeg_location": FFMPEG_PATH,
                "outtmpl": f"{folder}/%(title)s.%(ext)s",
                "ignoreerrors": True,
                "noplaylist": False,
                "progress_hooks": [progress_hook],
                "keepvideo": False,
            }

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
                text=f"❌ {e}"
            )

    threading.Thread(
        target=run,
        daemon=True
    ).start()

# ---------------- UI ---------------- #

title = ctk.CTkLabel(
    app,
    text="🎬 YouTube Downloader Pro",
    font=("Arial", 28, "bold")
)
title.pack(pady=20)

url_entry = ctk.CTkEntry(
    app,
    width=650,
    placeholder_text="Paste YouTube Video / Playlist URL"
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
    text="Select Quality"
).pack(pady=(15, 5))

ctk.CTkOptionMenu(
    app,
    variable=quality_var,
    values=["360p", "720p", "1080p"]
).pack()

ctk.CTkButton(
    app,
    text="⬇ Download",
    command=download_video,
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