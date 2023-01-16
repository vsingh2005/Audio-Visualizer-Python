from pydub import AudioSegment
import matplotlib.pyplot as plt
import sounddevice as sd
import numpy as np
import time

# File path for the audio file
file_path = "unsq.wav"

# Load audio file
audio = AudioSegment.from_file(file_path)
# Define a function to update the visualizer
def update_visualizer(data, rate):
    # Plot the audio data using matplotlib
    plt.clf()
    plt.plot(data)
    plt.pause(1/rate)
# Get the audio data and sample rate
data = np.array(audio.get_array_of_samples())
rate = audio.frame_rate

# Start the visualizer

plt.ion()
plt.show()

# Iterate over the audio data and update the visualizer in real-time
for i in range(0, len(data), rate):
    update_visualizer(data[i:i+rate], rate)
    time.sleep(1/rate)

plt.ioff()
plt.show()
