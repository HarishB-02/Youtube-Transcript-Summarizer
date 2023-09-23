from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo


yotube_video = "https://www.youtube.com/watch?v=BE-L7xu8pO4"

video_id = yotube_video.split("=")[1]
print(video_id)

YouTubeVideo(video_id)

YouTubeTranscriptApi.get_transcript(video_id)
transcript=YouTubeTranscriptApi.get_transcript(video_id)

print(transcript[0:5])

result = ""
for i in transcript:
    result += ' ' + i['text']
#print(result)
print(len(result))

summarizer = pipeline(task="summarization")

num_iters = int(len(result)/1000)
summarized_text = []
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  print("input text \n" + result[start:end])
  out = summarizer(result[start:end])
  out = out[0]
  out = out['summary_text']
  # print("Summarized text\n"+out)
  summarized_text.append(out)
print("\n\n\nSummarized")
print(str(summarized_text))
print("\n\n\nedited")
print(str(summarized_text[0:40]))
# len(str(summarized_text))



str(summarized_text)