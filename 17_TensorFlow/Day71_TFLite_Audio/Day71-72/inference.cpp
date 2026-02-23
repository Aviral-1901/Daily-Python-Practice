// #include <Arduino.h>
// #include "model_data.h"
// #include "test_input_float.h"
// #include "tensorflow/lite/schema/schema_generated.h" //model.h ma vako hex values bata meaning nikalna ko lagi
// #include "tensorflow/lite/micro/micro_error_reporter.h" //reports for any error while running the code and for debugging
// #include "tensorflow/lite/micro/micro_interpreter.h"
// #include "tensorflow/lite/micro/micro_mutable_op_resolver.h"
// //#include "tensorflow/lite/micro/all_ops_resolver.h"

// const int kTensorAreaSize = 80 * 1024;
// alignas(16) uint8_t tensor_arena[kTensorAreaSize];
// //alignas(16) will allow the array to start at memory address which is multiple of 16
// //tflite uses SIMD and needs (16bytes)128 bits of data at once
// //hardware inside can only grab 16-byte chunk so for this address must start with multiple of 16


// tflite::ErrorReporter* error_reporter = nullptr;
// const tflite::Model* model = nullptr;
// tflite::MicroInterpreter* interpreter = nullptr;
// TfLiteTensor* input = nullptr;
// TfLiteTensor* output = nullptr;

// void setup()
// {
//   Serial.begin(115200);
//   static tflite::MicroErrorReporter micro_error_reporter;
//   error_reporter = &micro_error_reporter;
//   model = tflite::GetModel(audio_model);
  
//   //static tflite::AllOpsResolver resolver;
//   static tflite::MicroMutableOpResolver<9> resolver; //<> to tell how many operations
//   //to know which operations to add, upload tflite file to netron.app 
//   resolver.AddConv2D();
//   resolver.AddRelu();
//   resolver.AddMaxPool2D();
//   resolver.AddReshape();
//   resolver.AddFullyConnected();
//   resolver.AddLogistic();
//   resolver.AddShape();
//   resolver.AddStridedSlice();
//   resolver.AddPack();

//   static tflite::MicroInterpreter static_interpreter(model, resolver, tensor_arena, kTensorAreaSize,
//                                                      error_reporter);
//   interpreter = &static_interpreter;
//   TfLiteStatus allocate_status = interpreter->AllocateTensors();
//   if (allocate_status != kTfLiteOk) 
//   {
//     TF_LITE_REPORT_ERROR(error_reporter, "AllocateTensors() failed");
//     while(1) {delay(100);}
//   }

//   input = interpreter->input(0);
//   output = interpreter->output(0);
// }

// void loop()
// {
//   float* input_buffer = input->data.f;
//   int index = 0;
//   for(int row=0; row<129; row++)
//   {
//     for(int col=0; col<124; col++)
//     {
//       if(row>=128 || col>=123) 
//         input_buffer[index] = 0.0f;
//       else
//       input_buffer[index] = input_float[row][col];
//       index++;
//     }
//   }

//   TfLiteStatus status = interpreter->Invoke();
//   if(status != kTfLiteOk)
//   {
//     TF_LITE_REPORT_ERROR(error_reporter, "Invoke failed");
//     return;
//   }

//   float prediction = output->data.f[0];
//   Serial.println(prediction);

// }


