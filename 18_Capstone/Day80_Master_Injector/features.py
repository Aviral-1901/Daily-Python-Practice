import numpy as np
import os
import scipy
import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path=r'C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day78_Serial_Injector\extraced.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

features = []
labels = []

def compute_stft(audio, frame_size, hop_size):
    spectrogram = []
    window = np.hamming(frame_size) 

    for i in range(0, len(audio)-frame_size + 1, hop_size):
        frame = audio[i: i+frame_size]
        frame = frame * window #widnowing the signal to prevent sharp edges
        fft_val = np.fft.fft(frame)
        mag = np.abs(fft_val)[: frame_size//2 + 1]
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


def get_features(file_path):
    spec = process_files(file_path)
    spec = (spec - 0.09) / 0.29
    input_data = spec.reshape(1, 129, 124, 1).astype(np.float32)
    # Set Input Tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)
    #run
    interpreter.invoke()
    #get features
    features = interpreter.get_tensor(output_details[0]['index'])
    
    return features.flatten()

if __name__ == "__main__":
    print(get_features(r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day78_Serial_Injector\yes.wav").shape)