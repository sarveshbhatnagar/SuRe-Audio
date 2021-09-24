import pafy
import os


url = "https://www.youtube.com/watch?v=erPS21mntMA"


def get_audio(url):
    video = pafy.new(url)

    bestaudio = video.getbestaudio()
    return bestaudio.download(filepath="../audio_files/"), bestaudio.filename


outpt, filename = get_audio(url)


def change_name(filename, newname):
    """
    rename the file to the new name
    """
    fileloc = os.path.join(os.path.abspath(".."), "audio_files")
    os.rename(os.path.join(fileloc, filename), os.path.join(fileloc, newname))
    return True
# def save_file(outpt):
#     current_file= open("")

# “../audio_files/filename.mp3”


change_name(filename, "test1.mp3")
# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=n06H7OcPd-g")
# yt = yt.get('mp4', '720p')
# yt.download('../audio_files/yt.mp3')
