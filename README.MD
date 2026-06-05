# 🎬 YouTube Downloader Pro

A modern YouTube Video & Playlist Downloader built with Python, CustomTkinter, yt-dlp, and FFmpeg.

## ✨ Features

- 📺 Download YouTube Videos
- 📋 Download Complete Playlists
- 🎥 360p / 720p / 1080p Quality Selection
- 🔊 Automatic Audio + Video Merge
- 📊 Download Progress Bar
- 📂 Open Download Folder
- 🎨 Modern CustomTkinter UI
- ⚡ Fast Downloads using yt-dlp
- 🖥️ Windows EXE Support

---

## 📸 Screenshot

Add your application screenshot here.

---

## 🛠️ Technologies Used

- Python 3
- CustomTkinter
- yt-dlp
- FFmpeg

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/RajeshKumar92828282/Youtube-video-download-.git
cd Youtube-video-download-
```

### Install Dependencies

```bash
pip install customtkinter
pip install yt-dlp
```

### Install FFmpeg

Download FFmpeg and extract it.

Update the path in the code:

```python
FFMPEG_PATH = r"YOUR_FFMPEG_BIN_PATH"
```

---

## ▶️ Run Project

```bash
python youtube_downloader.py
```

---

## 🔨 Build EXE

Install PyInstaller:

```bash
pip install pyinstaller
```

Build executable:

```bash
pyinstaller --onefile --windowed --collect-all customtkinter youtube_downloader.py
```

Output:

```text
dist/
└── youtube_downloader.exe
```

---

## 📁 Project Structure

```text
Youtube-video-download-
│
├── youtube_downloader.py
├── README.md
├── requirements.txt
├── build/
├── dist/
└── assets/
```

---

## 📜 Requirements

```text
customtkinter
yt-dlp
```

Create requirements file:

```bash
pip freeze > requirements.txt
```

---

## 👨‍💻 Author

Rajesh Kumar Behera

GitHub:
https://github.com/RajeshKumar92828282

---

## ⭐ Support

If you like this project, give it a star on GitHub.