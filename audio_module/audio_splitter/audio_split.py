from pydub import AudioSegment
import math
import os


class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = os.path.join(folder, filename)

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 100
        t2 = to_min * 60 * 100
        split_audio = self.audio[t1:t2]
        split_audio.export(os.path.join(
            self.folder, split_filename), format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 6)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


folder = '../../audio_files'

audio_file = 'fileaudio.wav'

split_wav = SplitWavAudioMubin(folder, audio_file)

split_wav.multiple_split(min_per_split=1)
