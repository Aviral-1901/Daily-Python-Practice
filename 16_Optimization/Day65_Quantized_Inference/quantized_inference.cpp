#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include "audio_model.h"
#include "test_input_int.h"

const uint8_t INPUT_Z = 54;
const uint8_t WEIGHT_Z = 115;
const uint8_t CONV_OUT_Z = 81;
const uint32_t MULTIPLIER = 50;
const uint8_t SHIFT = 16;
const uint8_t DENSE_WEIGHT_Z = 130;
const int32_t M_DENSE = 18874;
const uint8_t DENSE_SHIFT = 16;

int main()
{
    
    uint8_t weight[128][3];
    memset(weight, 115, sizeof(weight));
    uint8_t output[8][121] = {0};

    for(int flt=0; flt<8; flt++)
    {
        for(int t=0; t<121; t++)
    {
        int32_t accumulator = 0;
        for(int row=0; row<128; row++)
        {
            for(int k=0; k<3; k++)
            {
                int32_t val = (int32_t)test_input_int[row][t+k] - INPUT_Z;
                int32_t w = (int32_t)conv_weights[flt][row][k] - WEIGHT_Z;
                accumulator += val * w;
            }
        }
        int32_t rescaled = (accumulator * MULTIPLIER) >> SHIFT;
        int32_t final_val = rescaled + CONV_OUT_Z;
        if(final_val< CONV_OUT_Z) final_val = CONV_OUT_Z;  //ReLU
        if(final_val>255) final_val = 255;
        output[flt][t] = final_val;
    }
    }

    //max pooling
    uint8_t pooled_out[8][60];
    for(int f=0; f<8; f++)
    {
        for(int t=0; t<60; t++)
        {
            int start = t*2;
            int end = start + 2;
            if(output[f][start] >= output[f][start+1]) pooled_out[f][t] = output[f][start];
            else pooled_out[f][t] = output[f][start+1];
        }
    }

    //dense layer
    int32_t dense_sum = 0;
    for(int f=0; f<8; f++)
    {
        for(int t=0; t<60; t++)
        {
            int idx = (f * 60) + t;
            int32_t val = (int32_t)pooled_out[f][t] - CONV_OUT_Z;
            int32_t w = (int32_t)dense_weights[idx][0] - DENSE_WEIGHT_Z;
            dense_sum += val * w;
        }
    }

// Add the bias here (assuming it's scaled correctly)
    int32_t prediction = ((dense_sum * M_DENSE) >> DENSE_SHIFT) + 0;

    // Clamp the result to the 8-bit range (0-255)
    if (prediction > 255) prediction = 255;
    if (prediction < 0)   prediction = 0;

    if(prediction > 128) printf("AI output : Yes (%d)\n",prediction);
    else printf("AI output : No (%d)\n",prediction);
}