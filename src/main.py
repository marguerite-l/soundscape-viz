import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load audio
rate, data = wavfile.read("data/XC924056 - Savannah Sparrow - Passerculus sandwichensis.wav")

# Info about the audio file
print("Sample rate:", rate)
print("Audio shape:", data.shape)  #(total samples, channels)

# Create spectrogram
plt.figure(figsize=(10, 4))
plt.specgram(data, Fs=rate)
plt.title("Environmental Noise Spectrogram")
plt.xlabel("Time")
plt.ylabel("Frequency")

# Save image
plt.savefig("results/spectrogram.png")

print("Spectrogram saved.")
