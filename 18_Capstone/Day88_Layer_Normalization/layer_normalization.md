In deep network (like 96 layer GPT model), continuous matrix multiplication across the layers causes gradients to grow exponentially(exploding gradients) or shrink(vanishing gradients) so information is lost.
We use a SKIP Connection or Residual Connection to solve this.

Math: Output = Attention(X) + X
By adding original input X to the output allows positional encoding and original word meaning to survive through all layers.
Addition ensures the error signal can travel backward to the first layer without being shrunk by multiplications.

Only adding could also cause the numbers to grow large so we normalize the numbers.
At first we find the average of the word vector.
Center it by subtracting the average so now mean = 0.
Shrink the numbers to a standard range (-1 to 1).
It preserves the pattern but resets the scale and smaller numbers keeps everything stable.