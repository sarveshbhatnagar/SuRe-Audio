from __future__ import unicode_literals
# import pafy
import os
# from tube_dl import Youtube
import youtube_dl


url = "https://www.youtube.com/watch?v=EeDnoTdLvh0"


def get_audio(url, dest=""):

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return True


out_file = get_audio(url)

# TODO check breaking changes


def change_name(filepath, newname):
    """
    rename the file to the new name
    """
    fileloc = os.path.join(os.path.abspath(".."), "audio_files")
    os.rename(filepath, os.path.join(fileloc, newname))
    return True


change_name(out_file, "test1.mp4")
