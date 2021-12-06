
from youtube_transcript_api import YouTubeTranscriptApi
import transcribe_agent.transcribe as tr
from gensim.summarization import summarize
from gensim.summarization import keywords
# Why this wont work? Sometimes the transcript api wont give punctuations.


th = tr.Transcriber("XO97Uon83Os")
th.load_transcript("sometranscript")
# th.transcribe()
# th.save_transcript("sometranscript1")

tt = tr.TTexts(th.transcript)
text = tt.get_complete_text()
print(summarize(text, ratio=0.1))
# from nltk.corpus import stopwords
# print(stopwords.word('english'))
# th = tr.Transcriber("J8Eh7RqggsU")
# th.transcribe()
# th.save_transcript("transcript123")

# th.load_transcript("transcript123")

