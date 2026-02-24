input_path = r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day76_Feature_Extraction\extraced.tflite"

with open(input_path, 'rb') as f:
    tflite_data = f.read()
    #tflite_data ma model ko raw bytes store hunxa

    hex_lines = []
    for i, byte in enumerate(tflite_data):
        hex_str = f"0x{byte:02x}" #byte lai hex (0x00) ma change gareko
        hex_lines.append(hex_str)
    
    c_lines = []
    for i in range(0, len(hex_lines), 12):
        chunk = hex_lines[i : i+12] #12 ota hex values ko euta chunk liyem
        line = ", ".join(chunk) #chunk lai comma le join garera euta line banako
        c_lines.append(f" {line}")
    
    c_array = ", \n".join(c_lines) #c_lines lai join garera full array banako

    model_len = len(tflite_data)

header_file_path = r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day76_Feature_Extraction\extractor_model.h"

header_content = f"""
#ifndef EXTRACTOR_MODEL_DATA_H
#define EXTRACTOR_MODEL_DATA_H

const unsigned char extractor_model[] = {{
{c_array}
}};

const int extractor_model_len = {model_len};

#endif 
"""

with open(header_file_path, "w") as f:
    f.write(header_content)
