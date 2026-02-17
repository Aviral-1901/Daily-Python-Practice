#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "final_model.h"

//i am still learning and for some reason i am getting NO for sample_yes and YES for sample_no
//so i will be looking into it and try to fix with what is wrong

const uint8_t INPUT_Z = 54;
const uint8_t WEIGHT_Z = 115;
const uint8_t CONV_OUT_Z = 81;
const uint32_t MULTIPLIER = 50;
const uint8_t SHIFT = 16;
const uint8_t DENSE_WEIGHT_Z = 130;
const int32_t M_DENSE = 18874;
const uint8_t DENSE_SHIFT = 16;

int main() {
   
    const uint8_t (*current_test)[123] = sample_yes; 

    uint8_t output[8][121];

   
    for(int flt=0; flt<8; flt++) {
        for(int t=0; t<121; t++) {
            int32_t acc = 0;
            for(int row=0; row<128; row++) {
                for(int k=0; k<3; k++) {
                    acc += ((int32_t)current_test[row][t+k] - INPUT_Z) * 
                           ((int32_t)conv_weights[flt][row][k] - WEIGHT_Z);
                }
            }
            int32_t rescaled = (acc * MULTIPLIER) >> SHIFT;
            int32_t val = rescaled + CONV_OUT_Z;
            if (val < CONV_OUT_Z) val = CONV_OUT_Z; // ReLU
            if (val > 255) val = 255;
            output[flt][t] = (uint8_t)val;
        }
    }

   
    uint8_t pooled[8][60];
    for(int f=0; f<8; f++) {
        for(int t=0; t<60; t++) {
            uint8_t v1 = output[f][t*2];
            uint8_t v2 = output[f][t*2 + 1];
            pooled[f][t] = (v1 > v2) ? v1 : v2;
        }
    }

   
    int32_t dense_sum = dense_bias_int;
    for(int f=0; f<8; f++) {
        for(int t=0; t<60; t++) {
            int idx = (f * 60) + t;
            dense_sum += ((int32_t)pooled[f][t] - CONV_OUT_Z) * 
                         ((int32_t)dense_weights[idx][0] - DENSE_WEIGHT_Z);
        }
    }

    int32_t prediction = ((dense_sum * M_DENSE) >> DENSE_SHIFT);   
    if (prediction > 255) prediction = 255;
    if (prediction < 0)   prediction = 0;

    printf("RAW PREDICTION: %d\n", prediction);
    printf("Result: %d (%s)\n", prediction, (prediction > 128) ? "YES" : "NO");
    return 0;
}