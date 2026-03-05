import serial
import struct
import time
import numpy as np

# --- 1. SETUP ---
# CHANGE 'COM8' to your actual port if it changed
ser = serial.Serial("COM8", 115200, timeout=5.0) 
time.sleep(2) # Crucial: Wait for ESP32 to reboot after connection

# --- 2. HELPER FUNCTIONS ---
def get_features(label_val):
    # DUMMY DATA FOR TESTING THE PIPELINE
    # If label=1 (YES), send a vector of 1.0s
    # If label=0 (NO), send a vector of 0.0s
    # If label=2 (TEST), send a vector of 0.9s
    if label_val == 1:
        return [1.0] * 488
    elif label_val == 0:
        return [0.0] * 488
    else:
        return [0.9] * 488

def calculate_checksum(byte_data):
    total = 0
    for b in byte_data:
        total = (total + b) % 256
    return total

# --- 3. THE SENDER ---
def send_and_wait(command, label, features):
    # Flush old garbage
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    # Pack Data
    header = b'START'
    cmd_label = struct.pack('BB', command, label)
    payload = struct.pack('488f', *features)
    chksum = calculate_checksum(payload)
    chksum_byte = struct.pack('B', chksum)

    packet = header + cmd_label + payload + chksum_byte
    
    # Send ALL AT ONCE (ESP32 buffer is usually big enough for 2KB if read fast)
    ser.write(packet)

    # Wait for ESP32 to reply
    print("Waiting for ESP32...")
    while True:
        # Read whatever the ESP32 says
        reply = ser.readline().decode('utf-8', errors='ignore').strip()
        
        if reply:
            print(f"ESP32 says: {reply}")
            
        # Break the loop if we get the final confirmation
        if "Learned" in reply or "Predicted" in reply or "Error" in reply:
            break

# --- 4. THE EXECUTION SEQUENCE ---
print("\n--- TEACHING YES ---")
feat_yes = get_features(1)
send_and_wait(1, 1, feat_yes)

print("\n--- TEACHING NO ---")
feat_no = get_features(0)
send_and_wait(1, 0, feat_no)

print("\n--- ASKING PREDICTION ---")
feat_test = get_features(2) # 0.9 is closer to YES (1.0) than NO (0.0)
send_and_wait(2, 0, feat_test)

print("\nFinished.")