from flask import Flask,render_template,request
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo

app = Flask("__name__")



@app.route('/', methods=['POST','GET'])
def home():
    if request.method=='POST':
        youtube_video = request.form['youtubelink']
        video_id = youtube_video.split("=")[1]
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
        st=[]
        for i in range(0, num_iters + 1):
            start = 0
            start = i * 1000
            end = (i + 1) * 1000
            # print("input text \n" + result[start:end])
            out = summarizer(result[start:end])
            out = out[0]
            out = out['summary_text']
            st.append(out)
            print(st[:1])
        return render_template("output.html",outt=" ".join(st[:1]))
    else:
        return render_template('home.html')
    
# def transcript_summarizer(yotube_video):
    
if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)


    
# @app.route('/output')
# def output():
#     return render_template("output.html", str(st))
