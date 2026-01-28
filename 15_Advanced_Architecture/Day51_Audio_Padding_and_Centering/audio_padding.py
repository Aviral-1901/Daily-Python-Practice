import numpy as np
import scipy 
import matplotlib.pyplot as plt

def pad_to_1sec(audio):
    if len(audio) > 16000:
        audio = audio[:16000]
    
    if len(audio) < 16000:
        pad_total = 16000 - len(audio)
        pad_left = pad_total // 2
        pad_right = pad_total - pad_left
        audio = np.pad(audio, (pad_left, pad_right), 'constant')
    
    return audio

rate, data = scipy.io.wavfile.read(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day51_Audio_Padding_and_Centering\yes.wav")

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

final_audio = pad_to_1sec(clean_audio)
print("Final length :",len(final_audio))
plt.plot(final_audio)
plt.show()