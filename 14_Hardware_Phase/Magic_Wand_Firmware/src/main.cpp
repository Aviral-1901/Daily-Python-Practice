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
    
    if(prediction > 0.8)
    {
      Serial.println("Walking |||||||||");
      digitalWrite(LED_PIN,HIGH);
    }
    else if(prediction < 0.4) //neural-network while training gave 0.32 for sitting so i have used 0.4 as threshold here
    {
      Serial.println("..............");
      digitalWrite(LED_PIN,LOW);
    }
    // else
    // {
    //   Serial.print("unsure: ");
    //   Serial.println(prediction);
    // }
  }
 }
}



/* 
what i did in day31 during learning
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
*/


/*
what i did in day32 learning
Adafruit_MPU6050 my_mpu;

void setup()
{
  Serial.begin(115200);
  if(!my_mpu.begin())
  {
    while(1);
  }
  

}

void loop()
{
  sensors_event_t accel_data;
  sensors_event_t gyro_data;
  sensors_event_t temp_data;
  my_mpu.getEvent(&accel_data, &gyro_data, &temp_data);
  Serial.print("Acceleration : ");
  Serial.println(accel_data.acceleration.z);
  delay(500);
}
*/