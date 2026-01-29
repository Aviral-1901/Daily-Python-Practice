import numpy as np
import os
import scipy

script_dir = os.path.dirname(os.path.abspath(__file__))


features = []
labels = []


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



def process_files(file):
    rate, data = scipy.io.wavfile.read(file)
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
    
    if len(clean_audio) > 16000:
        clean_audio = clean_audio[:16000]

    if len(clean_audio) < 16000:
        pad_total = 16000 - len(clean_audio)
        pad_left = pad_total // 2
        pad_right = pad_total - pad_left
        clean_audio = np.pad(clean_audio, (pad_left, pad_right), 'constant')

    spectrogram = compute_stft(clean_audio, 256, 128)
    return np.log1p(spectrogram)




base_path = os.path.join(script_dir, "data")
categories = ["yes", "no"]

for label_name in categories:
    folder_path = os.path.join(base_path, label_name)

    file_list = os.listdir(folder_path)

    for filename in file_list:
        if filename.endswith(".wav"):
            full_path = os.path.join(folder_path, filename)
            img = process_files(full_path)
            features.append(img)

            if label_name == "yes":
                y = 1
            else:
                y = 0
            labels.append(y)

# Convert lists to NumPy Arrays
X = np.array(features)
Y = np.array(labels)

print("Raw Shape:", X.shape)
print("Y shape :",Y.shape)

# Calculate Global Stats
mean = np.mean(X)
std = np.std(X)

print(f"Global Mean: {mean:.4f}, Std: {std:.4f}")

# Apply Standardization
X = (X - mean) / std

print("Min in X:", np.min(X))
print("Max in X:", np.max(X))

# Save Everything
script_dir = os.path.dirname(os.path.abspath(__file__))
np.save(os.path.join(script_dir, "X_train.npy"), X)
np.save(os.path.join(script_dir, "Y_train.npy"), Y)
np.save(os.path.join(script_dir, "stats.npy"), np.array([mean, std]))

print("Dataset Saved.")