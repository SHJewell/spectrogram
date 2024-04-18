from pydub import AudioSegment
import numpy as np
from matplotlib import pyplot as plt


def extract_audio_data(filename):
    # Load the MP3 file
    audio = AudioSegment.from_file(filename, format="mp3")

    # Get the frame rate (sampling frequency)
    frame_rate = audio.frame_rate

    # Get the number of channels (e.g., mono=1, stereo=2)
    channels = audio.channels

    # Extract audio samples
    samples = np.array(audio.get_array_of_samples())

    # If stereo, reshape the array to have two columns
    if channels == 2:
        samples = samples.reshape((-1, 2))

    return samples, frame_rate


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    music_path = r"E:\Music\Podcasts\The Adventure Zone\TheAdventureZone001.mp3"

    samples, frame_rate = extract_audio_data(music_path)

    plt.plot(samples)
    plt.show()
