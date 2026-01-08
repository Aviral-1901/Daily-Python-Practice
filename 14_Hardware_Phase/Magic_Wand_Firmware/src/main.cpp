#include <Arduino.h>
#include "NeuralNetwork.h"
#include "RingBuffer.h"

RingBuffer rbuffer;
NeuralNetwork nn;
float current_batch[50];

void setup()
{
  Serial.begin(115200);
  Serial.println("System Initialized");
}

void loop()
{
  float input = 0.0;
  rbuffer.add(input);
  if(rbuffer.is_ready())
  {
    rbuffer.get_batch(current_batch);
    float prediction = nn.predict(current_batch);
    Serial.print("Prediction: ");
    Serial.println(prediction);
  }
  delay(100);
}