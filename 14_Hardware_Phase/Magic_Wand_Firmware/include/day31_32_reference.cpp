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