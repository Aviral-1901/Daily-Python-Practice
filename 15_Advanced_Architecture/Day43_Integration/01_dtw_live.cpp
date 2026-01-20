#include <stdio.h>
#include <cmath>
#include <cstring>
#include "templates.h"

struct Point3d
{
    float x; float y; float z;
};

float min3(float a, float b, float c)
{
  float m = a;
  if(b < m) m = b;
  if(c < m) m = c;
  return m;
}

float dtw(const float template_data[][3], Point3d* live_data)
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

int main()
{
    Point3d live_data[111];

    //fill live data with template data for checking
    for(int k=0; k<111; k++)
    {
        live_data[k].x = templates[k][0];
        live_data[k].y = templates[k][1];
        live_data[k].z = templates[k][2];
    }

    float result = dtw(templates, live_data);
    printf("Result: %f\n", result);
}