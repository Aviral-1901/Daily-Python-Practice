#include "NeuralNetwork.h"
#include "model_weights.h"
#include<math.h>

NeuralNetwork::NeuralNetwork()
{

}

float NeuralNetwork::sigmoid(float x)
{
    return 1 / (1 + expf(-x));
}

float NeuralNetwork::predict(float* input_array)
{
    for(int j=0; j<10; j++)
        {
            float layer1_sum = 0.0;
            for(int i=0; i<50; i++)
            {
                layer1_sum += input_array[i] * w1[i][j];
            }
            layer1_sum += b1[0][j];
            hidden_layer_out[j] = sigmoid(layer1_sum);
        }

        float layer2_sum = 0.0;
        for(int i=0; i<10; i++)
        {
            layer2_sum += hidden_layer_out[i] * w2[i][0];
        }
        layer2_sum += b2[0][0];
        return sigmoid(layer2_sum);
}