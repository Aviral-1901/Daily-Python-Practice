import serial
import struct
import time
from features import get_features

ser = serial.Serial("COM8", 115200)
time.sleep(2)

def send_and_wait(command, label, features):
    ser.write(b'START') #header

    ser.write(struct.pack('B', command)) 
    ser.write(struct.pack('B', label))

    payload = struct.pack('488f', *features)
    chunk_size = 256
    for i in range(0, len(payload), chunk_size):
        ser.write(payload[i:i+chunk_size])
        time.sleep(0.01)

    while True:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(line)
        if "Learned" in line or "Predicted" in line:
            break



feat_yes = get_features(r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day80_Master_Injector\yes.wav")
print("Teaching esp32 yes")
send_and_wait(1, 1, feat_yes)
feat_no = get_features(r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day80_Master_Injector\no.wav")
print("Teaching esp32 no")
send_and_wait(1, 0, feat_no)
print("Extracting test features")
feat_test = get_features(r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day80_Master_Injector\test_yes.wav")
print("Asking esp32 for prediction")
send_and_wait(2, 0, feat_test)