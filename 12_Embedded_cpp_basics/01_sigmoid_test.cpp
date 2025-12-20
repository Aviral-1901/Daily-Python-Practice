#include<stdio.h>
#include<iostream>
#include<math.h>

using namespace std;

float sigmoid(float x)
{
    return 1.0 / (1.0 + exp(-x));
}

int main()
{
    float inputs[3] = {1.0, 2.0, 3.0};
    float weights[3] = {0.5, 0.25, 0.1};
    float bias = 0.2;
    float z = 0.0;
    for(int i = 0;i<3;i++)
    {
        z+= inputs[i] * weights[i];
    }

    z+= bias;
    float result = sigmoid(z);
    printf("The result is %f",result);
    return 0;
}