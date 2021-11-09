from youtube_transcript_api import YouTubeTranscriptApi
# YouTubeTranscriptApi.get_transcript(video_id)
import pickle
class Transcriber:
    def __init__(self,video_Id):
        ''' initilise video_Id from a youtube video 
        
            for eg.; https://www.youtube.com/watch?v=kv-YXKRUheQ in this video link video_Id= 'kv-YXKRUheQ'
        '''
        self.video_Id=video_Id

    def transcribe(self):
        ''' creates a transcript of the video
            params:
                video_Id from class instance
            returns:
                transcript of the video
            saves:
                the transcript in self.transcript variable
        '''
        
        self.transcript=YouTubeTranscriptApi.get_transcript(self.video_Id)
        return self.transcript

    def save_transcript(self,filename):
        ''' creats a file and saves the transcript in this file
            params:
                filename
            save:
                the transcript in the file of users choice for the filename
        
        '''
        self.filename=filename
        with open(filename,'wb') as f:
            pickle.dump(self.transcript,f)

    def load_transcript(self,filename):
        ''' loads the transcript saved in the file
            params: 
                filename
            return:
                file with transcript stored
        
        '''
        self.filename=filename
        with open(filename,'rb') as f:
            filename=pickle.load(f)
            return filename


# steps to use Transcriber class
# th=Transcriber("kv-YXKRUheQ")
# th.transcribe()
# print(th.save_transcript("ABC"))
# print(th.load_transcript("ABC"))
