import struct
import serial
import time
from features import get_features

ser = serial.Serial('COM8', 115200)

def send_packet(command, label, features):
    ser.write(b'START') #header

    ser.write(struct.pack('B', command)) #'B' means unsigned char (1 byte)
    ser.write(struct.pack('B', label))

    #488f means 488 floats packed together
    payload = struct.pack('488f', *features)
    ser.write(payload)
    
    print(f"Sent {len(payload)} bytes of features")

while True:
    print("\n--- MENU ---")
    print("1. Teach YES")
    print("2. Teach NO")
    print("3. Predict Test")
    choice = input("Select: ")
    
    if choice == '1':
        feat = get_features(r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day78_Serial_Injector\yes.wav")
        send_packet(1, 1, feat) # Cmd=Learn, Label=1(Yes)
        
    elif choice == '2':
        feat = get_features(r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day78_Serial_Injector\no.wav")
        send_packet(1, 2, feat) # Cmd=Learn, Label=2(No)

    elif choice == '3':
        feat = get_features("test.wav") # (Record a test file!)
        send_packet(2, 0, feat) # Cmd=Predict, Label=Ignored

    time.sleep(0.5)
    while ser.in_waiting:
                print("ESP32:", ser.readline().decode().strip())
