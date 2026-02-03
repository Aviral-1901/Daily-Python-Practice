import numpy as np

class DenseLayer:  
    def __init__(self , n_inputs, n_neurons):
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons
        self.weights = np.random.randn(self.n_inputs,self.n_neurons) #random weights are for diversified learning and if used same weights then neurons give same output for same input and neurons are wasted known as symmetry problem or exact same blame 
        self.biases = np.zeros((1,self.n_neurons)) #harek neuron ko lagi individual bias dina ko lagi but 0 at starting
        self.inputs = None
        self.output = None

    def forward(self,inputs):
        self.inputs = inputs
        z = inputs @ self.weights + self.biases
        output = self.sigmoid(z)
        self.output = output
        return output

    def sigmoid(self,raw_sum):
        return 1 / (1 + np.exp(-raw_sum))
    
    def backward(self, output_error, learning_rate):
        slope = self.output * (1 - self.output)
        layer_gradient = slope * output_error
        input_error = layer_gradient @ self.weights.T
        weight_gradient = self.inputs.T @ layer_gradient
        self.weights += weight_gradient * learning_rate
        self.biases += np.sum(layer_gradient, axis=0) * learning_rate
        return input_error