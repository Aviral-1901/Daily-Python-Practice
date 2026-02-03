import numpy as np
from conv_layer import ConvLayer
from relu_layer import ReLU_Layer
from max_pool import MaxPool
from flatten_layer import FlattenLayer
from dense_layer import DenseLayer

class WakeWordModel:
    def __init__(self):
        self.conv = ConvLayer(8, 3, 128)
        self.relu = ReLU_Layer()
        self.pool = MaxPool(2, 2)
        self.flat = FlattenLayer()
        self.dense = DenseLayer(488, 1)
    
    def forward(self, X):
        result = self.conv.forward(X) 
        result = self.relu.forward(result)
        result = self.pool.forward(result)
        result = self.flat.forward(result)
        result = self.dense.forward(result)
        return result
    

data = np.random.randint(0, 256, size=16000)
data = data.reshape(1, 128, 125)

model = WakeWordModel()
out = model.forward(data)
print(out)
