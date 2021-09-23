import pafy
import os


url = "https://www.youtube.com/watch?v=dTu5dTEzVM4"
def get_audio(url):
    video = pafy.new(url)

    bestaudio = video.getbestaudio()
    return bestaudio.download(filepath="../audio_files/"), bestaudio.filename
outpt,filename=get_audio(url)

def change_name(filename,newname):
    with open("filenamewebm")


    



# def save_file(outpt):
#     current_file= open("")

# “../audio_files/filename.mp3” 


# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=n06H7OcPd-g")
# yt = yt.get('mp4', '720p')
# yt.download('../audio_files/yt.mp3')
