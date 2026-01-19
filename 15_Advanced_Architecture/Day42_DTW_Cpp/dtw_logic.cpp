#include <iostream>
#include <stdio.h>
#include <cmath>
#include <cstring>
#include "templates.h"

using namespace std;

float distance(int idx1, int idx2)
{
    float dx = templates[idx1][0]- templates[idx2][0];
    float dy = templates[idx1][1]- templates[idx2][1];
    float dz = templates[idx1][2]- templates[idx2][2];
    return sqrt(dx*dx + dy*dy + dz*dz);
}

float min3(float a, float b, float c)
{
  float m = a;
  if(b < m) m = b;
  if(c < m) m = c;
  return m;
}

float dtw()
{
    float prev_row[111], curr_row[111];
    //set all elements of previous row to infinity
    for(int i=0; i<111; i++)
    {
      prev_row[i] = INFINITY;
      curr_row[i] = INFINITY;
    }
    //find the value for first element of previous row which is the top row
    prev_row[0] = distance(0, 0);

    //handling top row
    for(int i=1; i<111;i++)
    {
      prev_row[i] = distance(0, i) + prev_row[i-1];
    }

    for(int i=1; i<111; i++)
    {
      curr_row[0] = distance(i, 0) + prev_row[0]; //handling left column
      for(int j=1; j<111; j++)
      {
        curr_row[j] = distance(i, j) + min3(prev_row[j], prev_row[j-1], curr_row[j-1]);
      }
      memcpy(prev_row, curr_row, sizeof(prev_row)); //copy curr_row to prev_row
      //memcpy(destination, source, sizeof(source))
    }
  
  return prev_row[110];
}

int main()
{
  float final_value = dtw();
  printf("The final value is %f",final_value);
}