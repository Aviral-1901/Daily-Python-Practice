#include<stdio.h>
#include<math.h>
#include "model_weights.h"

float sigmoid(float x)
{
    return 1.0 / (1.0 + exp(-x));
}

int main()
{
    float testInputs[4][2] = {{0,0}, {0,1}, {1,0}, {1,1}};
    float h[3]; //to hold hidden layer neuron's output
    float inputs[2]; 
    for(int k =0; k<4; k++)
    {
        printf("Input: %f %f -> ",testInputs[k][0],testInputs[k][1]);
        inputs[0] = testInputs[k][0];
        inputs[1] = testInputs[k][1];

    for(int j= 0;j<3;j++)  //to loop over 3 hidden neurons
    {
        float z = 0.0;
        for(int i=0; i<2; i++)  //to loop over 2 inputs
        {
            z += inputs[i] * w1[i][j];  // z = sum of (input × weight) -> z = w1*x1 + w2*x2
        }
        z += b1[0][j];   //add bias to the raw sum for that  neuron
        h[j] = sigmoid(z);  // convers raw sum to limit between 0 and 1
    }

    // for(int i =0;i<3;i++)
    // {
    //     printf(" %f",h[i]);  //print values of 3 hidden layer outputs
    // }

    float final_z = 0.0;  //raw sum for final neuron
    for(int i= 0; i<3;i++)
    {
        final_z += h[i] * w2[i][0];   //calculate raw sum for final neuron z = w1*x1 + w2*x2
    }
    final_z += b2[0][0];  //add bias to raw sum
    float final_prediction = sigmoid(final_z); //final layer output/prediction

    printf("Prediction: %f\n", final_prediction);
    }
}