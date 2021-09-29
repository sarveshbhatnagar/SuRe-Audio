# from bs4 import BeautifulSoup as bs
# import requests

# from bs4 import BeautifulSoup
# import requests

# def getPlaylistLinks(url):
#     sourceCode = requests.get(url).text
#     soup = BeautifulSoup(sourceCode, 'html.parser')
#     domain = 'https://www.youtube.com'
#     print('hello1')
#     for link in soup.find_all("a", {"dir": "ltr"}):
#         href = link.get('href')
#         print("hello2")
#         if href.startswith('/watch?'):
#             print("hello3")
#             print(link.string.strip())
#             print(domain + href + '\n')

# getPlaylistLinks('https://www.youtube.com/watch?v=tt2k8PGm-TI&list=RDMM4fndeDfaWCg&index=4')

from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': False
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(
        ['https://youtu.be/bpg6RSHS4Zc'])


'''
transfering downloaded files to audio_files folder 
'''


def change_name(filename, newname):
    """
    rename the file to the new name
    """
    fileloc = os.path.join(os.path.abspath(".."), "audio_files")
    os.rename(os.path.join(fileloc, filename), os.path.join(fileloc, newname))
    return True


'''
tasks left to do
1)find the names of the all the files downloading
2)Use the names to change the path of the downloaded files using change_name function'''
