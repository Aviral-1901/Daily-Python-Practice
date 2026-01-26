import scipy
import numpy as np
import matplotlib.pyplot as plt

rate, data = scipy.io.wavfile.read(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day49_Audio_Processing\yes.wav", )

 #Check if stereo (2 dimensions)
if len(data.shape) > 1:
    data = data[:, 0] 

max_volume = data.max()
threshold = 0.1 * max_volume

start = 0
for i in range(len(data)):
    if(np.abs(data[i]) > threshold):
        start = i
        break

end = len(data)
for i in range(len(data)-1, 0, -1): # Loop backwards
    if np.abs(data[i]) > threshold:
        end = i
        break

clean_audio = data[start:end]
print(len(clean_audio))
print("duration is :",len(clean_audio) / 16000)

plt.figure(figsize=(10, 4))
plt.plot(data, label="Raw", alpha=0.5)
plt.plot(range(start, end), clean_audio, label="Trimmed", color='red')
plt.legend()
plt.show()