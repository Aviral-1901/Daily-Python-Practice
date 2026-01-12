#include <Arduino.h>
#include "NeuralNetwork.h"
#include "RingBuffer.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

RingBuffer rbuffer;
NeuralNetwork nn;
Adafruit_MPU6050 my_mpu;
float gravity = 0.0;
float current_batch[50];
float prediction = 0.0;
const int LED_PIN = 2;
unsigned int previous = 0;
bool is_walking = false; //Tracks the current system state (Sitting vs Walking)

void setup()
{
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(115200);
  if(!my_mpu.begin())
  {
    while(1);
  }
  //to warm up the filter instantly
  sensors_event_t a, g, t;
  my_mpu.getEvent(&a, &g, &t);
  gravity = a.acceleration.z; // Start at the correct valuel
}

void loop()
{
  if(millis()- previous > 10)
  {
    previous = millis();
  sensors_event_t accel_data;
  sensors_event_t gyro_data;
  sensors_event_t temp_data;

  my_mpu.getEvent(&accel_data, &gyro_data, &temp_data);
  float raw_z = accel_data.acceleration.z;
  float alpha = 0.1;  //smoothing factor
  //low pass filter and lets gravity to change slowly over time 
  gravity = (alpha * raw_z) + ((1 - alpha) * gravity); //gravity = (0.1 * gravityNew[input]) + (0.9 * gravityOld)  -> i gave more weightage to the old value(90%)
  float user_acc = raw_z - gravity; //high pass filter
  user_acc /= 20;  //normalizatio
  rbuffer.add(user_acc);  //added the value to ring-buffer
  if(rbuffer.is_ready())
  {
    rbuffer.get_batch(current_batch);
    prediction = nn.predict(current_batch);
    
    //uses two thresholds to prevent LED flickering.
    if(!is_walking)
    {
    if(prediction > 0.8)
    {
      Serial.println("Walking |||||||||");
      digitalWrite(LED_PIN,HIGH);
      is_walking = true;
    }
  }
  else if(is_walking)
  {
    if(prediction < 0.4) //neural-network while training gave 0.32 for sitting so i have used 0.4 as threshold here
    {
      Serial.println("..............");
      digitalWrite(LED_PIN,LOW);
      is_walking = false;
    }
  }
  }
 }
}



