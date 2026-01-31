"""
POOL SIZE EXPLAINED:
--------------------
Think of this as the "Summary Window."
If pool_size = 2, we look at 2 time steps and pick the winner.
- Input:  [1, 5, 2, 8]
- Window 1: [1, 5] -> Max is 5
- Window 2: [2, 8] -> Max is 8
- Output: [5, 8]

Effect: Reduces data size by factor of (1/Stride).
Benefit: Makes the AI indifferent to small shifts in time (Translation Invariance).
"""
import numpy as np

class MaxPool:
    def __init__(self, pool_size, stride):
        self.pool_size = pool_size
        self.stride = stride
    
    def forward(self, input_data):
        batch, num_filters, input_width = input_data.shape
        output_width = (input_width - self.pool_size) // self.stride + 1
        output = np.zeros((batch, num_filters, output_width))

        for b in range(batch):
            for f in range(num_filters):
                for t in range(output_width):
                    start = t * self.stride
                    end = start + self.pool_size
                    window = input_data[b, f, start:end]
                    output[b, f, t] = np.max(window)

        return output
    


pool = MaxPool(2,2)

data = np.random.randn(1, 1, 10)

out = pool.forward(data)

print(out.shape)


        
