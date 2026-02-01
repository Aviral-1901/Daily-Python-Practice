import numpy as np

class ReLU_Layer:
    def __init__(self):
        pass
    
    def forward(self, input_data):
        return np.maximum(0, input_data)
    

data = np.array([-10, 5, 0, -2, 8])

relu = ReLU_Layer()
out = relu.forward(data)
print(out)