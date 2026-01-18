import numpy as np
import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "templates.h")

def load_gesture(filename):
    df = pd.read_csv(filename)
    df = df.rolling(window=5, min_periods=1).mean()
    acceleration_data = df[["Acceleration x (m/s^2)","Acceleration y (m/s^2)","Acceleration z (m/s^2)"]]
    acceleration_data = acceleration_data - acceleration_data.mean(axis=0) #remove gravity
    acceleration_data = acceleration_data / np.abs(acceleration_data).max() #normalize the data
    numpy_matrix = acceleration_data.to_numpy()
    numpy_matrix = numpy_matrix[::20] #take every 20th points
    return numpy_matrix

def export_gesture(file, name, data):
    file.write(f"const float {name} [{data.shape[0]}][3] = {{\n")
    for row in data:
        text =  str(row.tolist()).replace('[','{').replace(']','}') 
        file.write(text + ",\n")
    file.write("};\n")


circle = load_gesture(r"C:\Users\Dell\Desktop\PYTHON Daily\15_Advanced_Architecture\Day41_EXport_Template\Circle.csv")

with open(file_path, 'w') as f:
    f.write(f"const int TEMPLATE_LENGTH = {circle.shape[0]};\n") # Add this! Critical for C++.
    f.write("#ifndef TEMPLATES_H\n")
    f.write("#define TEMPLATES_H\n")
    export_gesture(f, 'templates', circle)
    f.write("#endif")

