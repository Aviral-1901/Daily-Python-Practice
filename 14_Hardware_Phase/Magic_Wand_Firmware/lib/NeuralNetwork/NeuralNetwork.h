#ifndef NEURAL_NETWORK_H
#define NEURAL_NETWORK_H

class NeuralNetwork
{
    private:
    float hidden_layer_out [10];  //output of hidden layer,declared as class member so it avoids stack reallocation
    
    public:
    NeuralNetwork();
    float predict(float* input_array);
    float sigmoid(float x);

};

#endif