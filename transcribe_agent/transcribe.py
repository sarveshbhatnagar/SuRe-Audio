from youtube_transcript_api import YouTubeTranscriptApi
# YouTubeTranscriptApi.get_transcript(video_id)
import pickle


class Transcriber:
    def __init__(self, video_Id):
        ''' initilise video_Id from a youtube video 

            for eg.; https://www.youtube.com/watch?v=kv-YXKRUheQ in this video link video_Id= 'kv-YXKRUheQ'
        '''
        self.video_Id = video_Id

    def transcribe(self):
        ''' creates a transcript of the video
            params:
                video_Id from class instance

            returns:
                transcript of the video
            saves:
                the transcript in self.transcript variable
        '''

        self.transcript = YouTubeTranscriptApi.get_transcript(self.video_Id)
        # print(self.transcript)
        return self.transcript

    def save_transcript(self, filename):
        ''' creats a file and saves the transcript in this file
            params:
                filename
            save:
                the transcript in the file of users choice for the filename

        '''
        self.filename = filename
        with open(filename, 'wb') as f:
            pickle.dump(self.transcript, f)

    def load_transcript(self, filename):
        ''' loads the transcript saved in the file
            params: 
                filename
            return:
                file with transcript stored

        '''
        self.filename = filename
        with open(filename, 'rb') as f:
            filename = pickle.load(f)
            self.transcript = filename
            return filename

# Transcriber.transcribe("tcdVC4e6EV4")


class TText:
    """
    Simply converts transcript dict to TText instance for easy access
    """

    def __init__(self, transcript):
        ''' initilise transcript from a youtube video 

            for eg.; https://www.youtube.com/watch?v=kv-YXKRUheQ in this video link transcript= 'kv-YXKRUheQ'
        '''
        self.transcript = transcript
        self.text = transcript["text"]
        self.start = transcript["start"]
        # self.end = transcript["end"]
        self.duration = transcript["duration"]
        self.end = self.start + self.duration
        self.score = 0

    def set_score(self, score):
        ''' sets the tfidf score of the transcript
            params:
                transcript from class instance
            returns:
                score of the transcript
        '''
        self.score = score

    def get_text(self):
        ''' returns the transcript text
            params:
                transcript from class instance
            returns:
                text of the transcript
        '''
        return self.text

    def get_start(self):
        ''' returns the start time of the transcript
            params:
                transcript from class instance
            returns:
                start time of the transcript
        '''
        return self.start

    def get_end(self):
        ''' returns the end time of the transcript
            params:
                transcript from class instance
            returns:
                end time of the transcript
        '''
        return self.end


class TTexts:
    """
    TTexts class contains transcripts of TText type.

    How to use: Transcribe->call TTexts on the result.
    e.g. 
    th = Transcribe(video_id="kv-YXKRUheQ")
    th.transcribe()
    tt=TTexts(th.transcript)
    """

    def __init__(self, transcripts, k=10):
        ''' initilise transcripts from a youtube video 

            for eg.; https://www.youtube.com/watch?v=kv-YXKRUheQ in this video link transcripts= 'kv-YXKRUheQ'
        '''
        self.transcripts = [TText(transcript) for transcript in transcripts]
        self.divide = k
        self.parts = len(self.transcripts) // self.divide
        if(self.parts != 0):
            self.parts_list = [transcripts[i:i + self.parts]
                               for i in range(0, len(transcripts), self.parts)]
        # print(self.parts_list)

    def get_complete_text(self):
        ''' returns the complete transcript text
            params:
                transcripts from class instance
            returns:
                text of the transcript
        '''
        texts = self.get_transcripts_text_list()
        return " ".join(texts)

    def get_transcripts_text_list(self):
        ''' returns the complete transcript text list
            params:
                transcripts from class instance
            returns:
                list of string of the transcript in parts
        '''
        return [transcript.get_text() for transcript in self.transcripts]

    def get_transcripts_start_list(self):
        ''' returns the complete transcript start time list
            params:
                transcripts from class instance
            returns:
                list of start time of the transcript in parts
        '''
        return [transcript.get_start() for transcript in self.transcripts]

    def get_transcripts_end_list(self):
        ''' returns the complete transcript end time list
            params:
                transcripts from class instance
            returns:
                list of end time of the transcript in parts
        '''
        return [transcript.get_end() for transcript in self.transcripts]


# steps to use Transcriber class
# th = Transcriber("kv-YXKRUheQ")
# th.transcribe()
# print(th.save_transcript("ABC"))
# print(th.load_transcript("ABC"))
