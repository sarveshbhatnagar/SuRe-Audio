from pydub import AudioSegment
# sound = AudioSegment.from_mp3("/path/to/file.mp3")
# sound.export("/output/path/file.wav", format="wav")


def convert_to_wav(file_path, output_path):
    """Converts mp4 file to wav"""
    sound = AudioSegment.from_mp3(file_path)
    sound.export(output_path, format="wav")
