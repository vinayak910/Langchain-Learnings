from youtube_transcript_api import YouTubeTranscriptApi

# Test with a known working video ID
video_id = 'dQw4w9WgXcQ' 

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    print("Success! First line:", transcript[0])

except Exception as e:
    print(f"Other error: {e}")