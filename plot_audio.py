import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open('output.wav', "rb")

sample_frequency = obj.getframerate()
n_samples = obj.getnframes()
singnal_wave = obj.readframes(n_samples) # or obj.readframes(-1)

obj.close()

time_audio = n_samples / sample_frequency
# print("Time: ", time_audio)

signal_array = np.frombuffer(singnal_wave, dtype=np.int16)
# print(signal_array.shape)

# time array
times = np.linspace(0, n_samples/sample_frequency, num=n_samples)

# plot the audio signal
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio Signal')
plt.ylabel('Signal Wave')
plt.xlabel('Time (s)')
plt.xlim(0, time_audio)
plt.show()