import numpy as np

class Neuron:
    def __init__(self):
        self.weight = np.random.rand()
        self.bias = 0.0

    def sigmoid(self,x):
        return 1 / (1 + np.exp(-x))
    
    def predict(self, input_data):
        z = self.weight * input_data + self.bias
        result = self.sigmoid(z)
        return result
    
    def train(self,input_x, target, learning_rate):
        prediction = self.predict(input_x)
        error = target - prediction
        slope = prediction * (1 - prediction)
        gradient = error * slope
        self.weight += gradient * input_x * learning_rate
        self.bias += gradient * learning_rate


my_neuron = Neuron()

for i  in range(10000):
    my_neuron.train(1.0, 1.0, 0.1)

result = my_neuron.predict(1.0)
print(result)