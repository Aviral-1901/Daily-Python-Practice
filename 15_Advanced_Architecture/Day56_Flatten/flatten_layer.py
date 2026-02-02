import numpy as np

class FlattenLayer:
    def __init__(self):
        pass
    def forward(self, input_data):
        batch, channel, width = input_data.shape  #channel = number of filters and width = width of filter/kernel
        flat_size = channel * width
        output = input_data.reshape(batch, flat_size)
        return output
    
data = np.arange(12) #flat list of 12 numbers
data = data.reshape(2, 2, 3) #reshape the flat list into the 3d shape we need for testing

flat = FlattenLayer()
output = flat.forward(data)
print(output)
print(output.shape)