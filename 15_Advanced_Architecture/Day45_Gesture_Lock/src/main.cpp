#include <Arduino.h>
#include "templates.h"
#include "RingBuffer3D.h"
#include <Adafruit_MPU6050.h>

float min3(float a, float b, float c)
{
  float m = a;
  if(b < m) m = b;
  if(c < m) m = c;
  return m;
}

float dtw(const float template_data[][3], Point3D* live_data)
{
    float prev_row[111], curr_row[111];
    //set all elements of previous row to infinity
    for(int i=0; i<111; i++)
    {
      prev_row[i] = INFINITY;
      curr_row[i] = INFINITY;
    }

    //find the value for first element of previous row which is the top row [0,0] of the matrix
    float t0x = template_data[0][0];
    float t0y = template_data[0][1];
    float t0z = template_data[0][2];

    float dx = t0x - live_data[0].x;
    float dy = t0y - live_data[0].y;
    float dz = t0z - live_data[0].z;
    prev_row[0] = (dx*dx + dy*dy + dz*dz);

    //handling top row
    for(int j=1; j<111; j++)
    {
      float dx = t0x - live_data[j].x;
      float dy = t0y - live_data[j].y;
      float dz = t0z - live_data[j].z;
      
      prev_row[j] = (dx*dx + dy*dy + dz*dz) + prev_row[j-1];
    }

    for(int i=1; i<111; i++)
    {
        //handling left-most column 
        float tx = template_data[i][0];
        float ty = template_data[i][1];
        float tz = template_data[i][2];

        float dx = tx - live_data[0].x;
        float dy = ty - live_data[0].y;
        float dz = tz - live_data[0].z;

        curr_row[0] = (dx*dx + dy*dy + dz*dz) + prev_row[0];

        for(int j=1; j<111; j++)
        {
            float lx = live_data[j].x;
            float ly = live_data[j].y;
            float lz = live_data[j].z;

            float dx = tx - lx;
            float dy = ty - ly;
            float dz = tz - lz;
            float cost = dx*dx + dy*dy + dz*dz;

            curr_row[j] = cost + min3(curr_row[j-1], prev_row[j], prev_row[j-1]);
        }
        memcpy(prev_row, curr_row, sizeof(prev_row)); //copy curr_row to prev_row

    }
  
  return prev_row[110];
}

Adafruit_MPU6050 mpu;
RingBuffer3D rb;
Point3D batch[111];
const float ALPHA = 0.1;
float gx = 0, gy = 0, gz = 0;

void setup()
{
  Serial.begin(115200);
  if(!mpu.begin())
  {
    Serial.println("Connection Failed");
    while(1);
  }
  //to warm up the filter instantly
  sensors_event_t a, g, t;
  mpu.getEvent(&a, &g, &t);
  gx = a.acceleration.x;
  gy = a.acceleration.y;
  gz = a.acceleration.z;

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  sensors_event_t acc;
  sensors_event_t gyro;
  sensors_event_t temp;
  mpu.getEvent(&acc, &gyro, &temp);
  
  // 1. Update Gravity Estimate
  gx = (ALPHA * acc.acceleration.x) + ((1.0 - ALPHA) * gx);
  gy = (ALPHA * acc.acceleration.y) + ((1.0 - ALPHA) * gy);
  gz = (ALPHA * acc.acceleration.z) + ((1.0 - ALPHA) * gz);

  // 2. Calculate User Movement (High Pass)
  float ux = acc.acceleration.x - gx;
  float uy = acc.acceleration.y - gy;
  float uz = acc.acceleration.z - gz;

  rb.add(ux, uy, uz);

  if(rb.is_ready())
  {
    rb.get_batch(batch);

    float max_val = 0.0;
    
    // Pass 1: Find Max
    for(int k=0; k<111; k++) 
    {
      float ax = fabs(batch[k].x);
      float ay = fabs(batch[k].y);
      float az = fabs(batch[k].z);
      if (ax > max_val) max_val = ax;
      if (ay > max_val) max_val = ay;
      if (az > max_val) max_val = az;
    }

    // Safety: Don't divide by zero or amplify noise
    if (max_val < 1.0) max_val = 1.0;
    // Pass 2: Normalize
    for(int k=0; k<111; k++) 
    {
      batch[k].x /= max_val;
      batch[k].y /= max_val;
      batch[k].z /= max_val;
    }
    // --- NORMALIZATION END ---

    float score = dtw(templates, batch);
    Serial.printf("Max: %.2f | Score: %.2f\n", max_val, score);
    if(score < 1000)
    {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else
      digitalWrite(LED_BUILTIN, LOW);
  }
  delay(50);
}