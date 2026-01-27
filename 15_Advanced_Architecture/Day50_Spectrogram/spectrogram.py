import numpy as np
import scipy
import matplotlib.pyplot as plt

def compute_stft(audio, frame_size, hop_size):
    spectrogram = []
    window = np.hamming(frame_size) 

    for i in range(0, len(audio)-frame_size, hop_size):
        frame = audio[i: i+frame_size]
        frame = frame * window #widnowing the signal to prevent sharp edges
        fft_val = np.fft.fft(frame)
        mag = np.abs(fft_val)[: frame_size//2]
        spectrogram.append(mag)
    
    return np.array(spectrogram).T

rate, data = scipy.io.wavfile.read(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day50_Spectrogram\yes.wav")

 #Check if stereo (2 dimensions)
if len(data.shape) > 1:
    data = data[:, 0] 

result = compute_stft(data, 256, 128)

spec_log = np.log1p(result) #log1p because if log(0) then it is -infinity for silence(0)

plt.imshow(spec_log, origin='lower', aspect='auto', cmap='jet')
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.show()
