from pytube import Playlist
from yt_dlp import YoutubeDL

def playlist_to_mp3(playlist_url, output_path):
    # 從播放清單URL創建Playlist對象
    # 設定下載選項，指定格式為 mp3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # 設定輸出路徑和檔名格式
        'outtmpl': output_path + '\\%(title)s.%(ext)s',
    }
    playlist = Playlist(playlist_url)
    
    # 遍歷播放清單中的每個視頻
    for video_url in playlist.video_urls:
        print(f"正在下載：{video_url}")
        try:
            # 下載視頻
            with YoutubeDL(ydl_opts) as ydl:
              ydl.download([video_url])
             
            print(f"已成功下載並轉換：{mp3_filename}")
        except Exception as e:
            print(f"錯誤：無法下載或轉換視頻 {video_url}，原因：{e}")

# 使用示例
playlist_url = 'https://www.youtube.com/playlist?list=PLtWhUGYRH7Mp3a8jAYK5kF9fcStzmPJM3'
output_path = 'D:\\GIT\\watermelon8157.github.io\\MP3\\心理敲敲門'
playlist_to_mp3(playlist_url, output_path)