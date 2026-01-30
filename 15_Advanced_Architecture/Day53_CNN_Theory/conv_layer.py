import numpy as np

class ConvLayer:
    def __init__(self, num_filters, kernel_size, input_height):
        self.weights = np.random.randn(num_filters, input_height, kernel_size)
        #num_filters = number of filters going to be used
        self.biases = np.zeros((num_filters, 1))
        
        self.k = kernel_size

    
    def forward(self, input_data):
        #input shape = (batch, height, width)
        batch_size, h, w = input_data.shape

        #output width = 125-3+1
        out_width = w - self.k + 1

        #output shape = batch, num_filters, out_width
        output = np.zeros((batch_size, len(self.weights), out_width))

        for b in range(batch_size):  #accessing the different audio 
            for f in range(len(self.weights)): #for each filter
                for t in range(out_width):    #slide across time

                    #slide the window from input
                    #take all frequencies, from time t to t+k
                    window = input_data[b, :, t:t+self.k]

                    #dot product -> Filter 'f' and the window
                    score = np.sum(window * self.weights[f])

                    #add the bias and store
                    output[b, f, t] = score + self.biases[f][0]

        return output           


X = np.random.randn(1, 128, 125)
layer = ConvLayer(8, 3, 128)

out = layer.forward(X)
print(out.shape)