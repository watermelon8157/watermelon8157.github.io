from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd

# 設定 YouTube 影片 ID
video_id = 'F7MJqvof24w'

# 擷取字幕
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# 將字幕轉換為 DataFrame
df = pd.DataFrame(transcript)

# 將 DataFrame 存入 CSV 檔案
df.to_csv('transcript.csv', index=False)