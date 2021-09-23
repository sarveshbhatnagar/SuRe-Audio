import pafy

url = "https://www.youtube.com/watch?v=dTu5dTEzVM4"
def get_audio(url):
    video = pafy.new(url)

    bestaudio = video.getbestaudio()
    return bestaudio.download()
get_audio(url)

