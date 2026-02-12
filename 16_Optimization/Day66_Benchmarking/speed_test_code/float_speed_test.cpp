// #include <Arduino.h>
// #include "test_input_float.h"
// #include <inttypes.h>
// #include "audio_model.h"


// void setup()
// {
//   Serial.begin(115200);
//   unsigned long int startTime = micros();
//       float conv_out[8][123] = {0.0};
//     float pool_out[8][61] = {0.0};
//     float final_score = 0.0;

//     //convolution
//     for(int flt=0; flt<8; flt++)
//     {
//         for(int t=0; t<121; t++)
//         {
//             float sum = 0.0;
//             for(int freq=0; freq<128; freq++)
//             {
//                 for(int k=0; k<3; k++)
//                 {
//                     sum += input[freq][t+k] * conv_weights[flt][freq][k];
//                 }
//             }
//             if(sum < 0) sum=0; //ReLU
//             conv_out[flt][t] = sum;
//         }
//     }


//     //max pooling
//     for(int f=0; f<8; f++)
//     {
//         for(int t=0; t<60; t++)
//         {
//             int start = t*2;
//             int end = t*2 + 2;
//             float max = 0.0;
//             if(conv_out[f][start] >= conv_out[f][start+1]) max = conv_out[f][start];
//             else max = conv_out[f][start+1];
//             pool_out[f][t] = max;
//         }
//     }

//     //dense layer
//     float sum = 0.0;
//     for(int f=0; f<8; f++)
//     {
//         for(int t=0; t<60; t++)
//         {
//             int idx = (f * 60) + t;
//             sum += pool_out[f][t] * dense_weights[idx][0];
//         }
//     }
//     sum += dense_biases[0][0];
//     float result = 1.0 / (1.0 + exp(-sum));
//     unsigned long int endTime = micros();
    
//     Serial.print("prediction : ");
//     Serial.println(result);
//     Serial.print("start : ");
//     Serial.println(startTime);
//     Serial.print("end : ");
//     Serial.println(endTime);

// }

// void loop()
// {

// }