import pydub
import numpy as np
from matplotlib import pyplot as plt
import scipy.fft as fft
import pathlib
from dataclasses import dataclass, field


@dataclass
class audioFile:
    audio_data: np.array = field(init=False)
    audio_file: pydub.AudioSegment = field(init=False)
    channels: int = field(init=False)
    format: str = field(init=False)
    bytes_per_sample: int = field(init=False)
    Fs: int = field(init=False)
    path: str = field(init=True)
    start_time: int = field(init=True, default=0)
    stop_time: int = field(init=True, default=None)


    def __post_init__(self):
        self.format = pathlib.Path(self.path).suffix[1:]

        with open(self.path) as raw_file:
            self.audio_file = pydub.AudioSegment.from_file(raw_file, format=self.format)

        # Get parameters
        self.channels = self.audio_file.channels
        self.Fs = self.audio_file.frame_rate
        self.bytes_per_sample = self.audio_file.sample_width


    def readAudioData(self, start_time=None, stop_time=None):

        if self.start_time == 0 and stop_time == None:
            self.audio_data = np.array(self.audio_file.get_array_of_samples())
        else:
            self.audio_data = np.array(self.audio_file.get_array_of_samples())[start_time:stop_time]

        # If stereo, reshape the array to have two columns
        if self.channels >= 2:
            self.audio_data = self.audio_data.reshape((-1, self.channels))

        return self.audio_data



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # guiFrame()

    pod_path = r"E:\Music\Podcasts\The Adventure Zone\TheAdventureZone001.mp3"
    song_path = r"E:\Music\Albums\Aesop Rock\Klutz [Explicit]\01-01- Klutz [Explicit].mp3"

    my_song = audioFile(song_path)

    fs = my_song.Fs
    ts = my_song.readAudioData()

    plt.plot(ts)
    plt.show()


# def extract_audio_data(filename, N: int = None, t0: int = 0):
#
#     if N and (t0 > N):
#             raise IndexError
#
#     # Load the MP3 file
#     audio = AudioSegment.from_file(filename, format="mp3")
#
#     # Get the frame rate (sampling frequency)
#     frame_rate = audio.frame_rate
#
#     # Get the number of channels (e.g., mono=1, stereo=2)
#     channels = audio.channels
#
#     #if N:
#
#
#     samples = np.array(audio.get_array_of_samples())
#
#     # If stereo, reshape the array to have two columns
#     if channels == 2:
#         samples = samples.reshape((-1, 2))
#
#     return samples, frame_rate

