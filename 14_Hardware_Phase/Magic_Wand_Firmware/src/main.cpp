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

void setup()
{
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
  sensors_event_t accel_data;
  sensors_event_t gyro_data;
  sensors_event_t temp_data;

  my_mpu.getEvent(&accel_data, &gyro_data, &temp_data);
  float raw_z = accel_data.acceleration.z;
  float alpha = 0.1;
  gravity = (0.1 * raw_z) + (0.9 * gravity);
  float user_acc = raw_z - gravity;
  user_acc /= 20;
  rbuffer.add(user_acc);
  if(rbuffer.is_ready())
  {
    rbuffer.get_batch(current_batch);
    prediction = nn.predict(current_batch);
    if(prediction > 0.8)
    {
      Serial.println("Walking |||||||||");
    }
    else
    {
      Serial.println("..............");
    }
  }
  delay(10);
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