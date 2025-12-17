import numpy as np

class DenseLayer:
    def __init__(self , n_inputs, n_neurons):
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons
        self.weights = np.random.randn(self.n_inputs,self.n_neurons) #random weights are for diversified learning and if used same weights then neurons give same output for same input and neurons are wasted known as symmetry problem or exact same blame 
        self.biases = np.zeros((1,self.n_neurons)) #harek neuron ko lagi individual bias dina ko lagi but 0 at starting

    def forward(self,inputs):
        z = inputs @ self.weights + self.biases
        output = self.sigmoid(z)
        return output

    def sigmoid(self,raw_sum):
        return 1 / (1 + np.exp(-raw_sum))
    
x = np.array([[1.0,2.0]]) # [[]] le batuxa ki yo 1x2 matrix ho ra it is important to keep 2 big brackets

layer1 = DenseLayer(2,5) #yo 5 neurons haru "HELPER NEURONS" ho they dont directly give the output but their output is important for final neuron to take decisions
layer2 = DenseLayer(5,1) #yo FINAL NEURON ho, yesle mathi ko 5 ota neuron ko weight linxa ra sabko lagi randomly weight assign garxa at first and at last everything is maintained based on the similar process of forward pass and back propagation
result1 = layer1.forward(x)
print("Output of layer 1 :",result1)
print("Shape of layer 1 :",result1.shape)

final_output = layer2.forward(result1)
print("Final Output :",final_output)
