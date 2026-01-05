#include<iostream>
#include<math.h>
#include "model_weights.h"

using namespace std;

float sigmoid(float x)
{
    return 1 / (1 + expf(-x));     // Using expf for single-precision (faster than exp for float)
}

class NeuralNetwork
{
    private:
    float hidden_layer_out [10];  //output of hidden layer,declared as class member so it avoids stack reallocation
    
    public:
    //hidden layer calculation
    float predict(float* input_array)
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

        //putput layer calculation
        float layer2_sum = 0.0;
        for(int i=0; i<10; i++)
        {
            layer2_sum += hidden_layer_out[i] * w2[i][0];
        }
        layer2_sum += b2[0][0];
        return sigmoid(layer2_sum);
    }
};

int main()
{
    float input[50] = {0}; //stack allocation:fast, initialized to 0 for testing

    NeuralNetwork nn;
    float result = nn.predict(input);
    cout<<"The final prediction is : "<<result;
}