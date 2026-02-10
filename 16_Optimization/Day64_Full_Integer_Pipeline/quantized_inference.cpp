#include <stdio.h>
#include <inttypes.h>
#include <string.h>

const uint8_t INPUT_Z = 54;
const uint8_t WEIGHT_Z = 115;
const uint8_t OUT_Z = 81;
const uint8_t MULTIPLIER = 50;
const uint8_t SHIFT = 16;

int main()
{
    uint8_t input[128][123];
    memset(input, 54, sizeof(input));
    uint8_t weight[128][3];
    memset(weight, 115, sizeof(weight));
    uint8_t output[121] = {0};

    for(int t=0; t<121; t++)
    {
        int32_t accumulator = 0;
        for(int row=0; row<128; row++)
        {
            for(int k=0; k<3; k++)
            {
                int32_t val = (int32_t)input[row][t+k] - INPUT_Z;
                int32_t w = (int32_t)weight[row][k] - WEIGHT_Z;
                accumulator += val * w;
            }
        }
        int32_t rescaled = (accumulator * MULTIPLIER) >> SHIFT;
        int32_t final_val = rescaled + OUT_Z;
        if(final_val< OUT_Z) final_val = OUT_Z;  //ReLU
        if(final_val>255) final_val = 255;
        output[t] = final_val;
    }

    //max pooling
    uint8_t pooled_out[60];
    for(int t=0; t<60; t++)
    {
        int start = t*2;
        int end = start + 2;
        if(output[start] >= output[start+1]) pooled_out[t] = output[t];
        else output[t] = pooled_out[t+1];
    }
    printf("%u",pooled_out[0]);    
}