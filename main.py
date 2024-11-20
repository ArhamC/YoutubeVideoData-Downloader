import yt_dlp

url = 'https://youtube.com/watch?v=2lAe1cqCOXo'

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    print("Title:", info_dict.get('title'))