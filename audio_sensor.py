import sounddevice as sd
import numpy as np

class AudioSensor:

    def __init__(self):
        self.duration = 1
        self.sample_rate = 44100

    def get_noise_level(self):

        recording = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1
        )

        sd.wait()

        volume = np.linalg.norm(recording) * 10

        return volume