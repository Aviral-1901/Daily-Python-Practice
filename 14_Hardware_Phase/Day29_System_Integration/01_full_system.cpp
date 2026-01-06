#include<iostream>
#include<math.h>
#include "model_weights.h"
#include<stdio.h>
using namespace std;

class RingBuffer
{   
    public:
    float buffer[50];  
    int head;          
    int count;        
    const int max_size = 50;  
    
    public:
    RingBuffer()
    {
        head = 0;    //at first head points at position 0
        count = 0;   //at first buffer is empty so count is 0
        for(int i=0; i<50; i++)
        {
            buffer[i] = 0.0;   //buffer ko sab index ma 0 haleko garbage na aaos vanera
        }
    }

    void add(float val)
    {
        buffer[head] = val;   //stores a value in current head position
        head++;               //head lai agi badauni to point next position
        if(head == max_size)
        {
            head = 0;   //head last position ma pugyo vane aba head lai 0 ma lagni
        }
        if(count != max_size)
        {
            count++;     //buffer ko size full vaye paxi count badhdaina
        }
    }

    bool is_ready()   //to check whether buffer is full or not
    {
        if(count==max_size)
        {
            return true;
        }
        return false;
    }

    float get(int index)   //return value at specific index of the buffer
    {
        return buffer[index];
    }

    void get_batch(float* output_array)
    {
        for(int i=0;i<max_size;i++)
        {
            int index = (head + i) % 50;
            output_array[i] = buffer[index];
        }
    }
};

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
    RingBuffer rbuffer;
    NeuralNetwork nn;
    float current_batch[50];
    float input_stream[55] = {}; //fills every index with 0
    input_stream[50] = input_stream[51]=input_stream[52]=input_stream[53]=input_stream[54] = 1;

    for(int i=0;i<55;i++)
    {
        rbuffer.add(float(input_stream[i]));

        if(rbuffer.is_ready())
        {
            rbuffer.get_batch(current_batch);
            float result = nn.predict(current_batch);
            printf("Sample %d: Prediction %f\n",i, result);
        }
        else
        {
            printf("Sample %d: Buffering....\n",i);
        }

    }
}

/*
 * ======================================================================================
 * NOTE: WHY 3 SAMPLES TRIGGER A POSITIVE DETECTION?
 * ======================================================================================
 * Observation: 
 * The buffer has 47 "Sitting" samples (0.0) and only 3 "Walking" samples (1.0).
 * Yet, the prediction jumps to ~0.93 (Walking). Why isn't it an average?
 * 
 * The Math Physics:
 * The Neural Network calculates a Weighted Sum (Dot Product):
 * z = (x0 * w0) + (x1 * w1) + ... + Bias
 * 
 * 1. The Power of Zero:
 *    The 47 "Sitting" samples are 0.0. 
 *    Math: 0.0 * Weight = 0.0.
 *    Result: They contribute NOTHING to the sum. They do not "pull the score down."
 *            They simply abstain from voting.
 * 
 * 2. The Power of Signal:
 *    The 3 "Walking" samples are 1.0.
 *    Math: 1.0 * Weight. 
 *    During training, the network learned that these inputs are critical features.
 *    Therefore, their Weights are likely high positive numbers.
 * 
 * 3. The Result:
 *    The sum accumulates rapidly because the Zeros don't cancel out the Ones.
 *    This acts like a "Trigger" or "Fire Alarm," not an "Average."
 * ======================================================================================
 */