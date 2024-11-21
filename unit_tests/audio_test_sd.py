import sounddevice as sd
from pydub import AudioSegment
import time

def play_mp3(file_path):
    sound = AudioSegment.from_mp3(file_path)
    # Convert to NumPy array
    samples = sound.get_array_of_samples()
    # Normalize the samples 
    samples = samples.astype('float32') / 32767 

    sd.play(samples, sound.frame_rate)
    time.sleep(10)
    sd.stop()
    # sd.wait()  # Wait for playback to finish


path = "../../Documents/test.mp3"
devices = sd.query_devices()
print("All devices:", len(devices), devices)
for i in range(len(devices)):
    device = devices[i]
    print(f"Playing audio on device: {i}: {device}")
    sd.default.device = i

    # Example usage
    play_mp3(path)