#include "RingBuffer3D.h"
RingBuffer3D::RingBuffer3D()
    {
        head = 0;
        count = 0;
    }
    
void RingBuffer3D::add(float x, float y, float z)
{
    buffer[head].x = x;
    buffer[head].y = y;
    buffer[head].z = z;
        
    head ++;

    if(head == 111)
        head = 0;

    if(count != 111)
        count++;     //buffer ko size full vaye paxi count badhdaina
}

void RingBuffer3D::get_batch(Point3D* output)
{
    for(int i=0; i<111; i++)
    {
        int index = (head + i) % 111;
        output[i] = buffer[index]; 
    }
}

bool RingBuffer3D::is_ready()   //to check whether buffer is full or not
{
    return count >= 111;
}
