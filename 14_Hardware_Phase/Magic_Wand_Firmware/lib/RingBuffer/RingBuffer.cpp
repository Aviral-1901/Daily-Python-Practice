#include "RingBuffer.h"

RingBuffer::RingBuffer()
    {
        head = 0;    //at first head points at position 0
        count = 0;   //at first buffer is empty so count is 0
        for(int i=0; i<50; i++)
        {
            buffer[i] = 0.0;   //buffer ko sab index ma 0 haleko garbage na aaos vanera
        }
    }

void RingBuffer::add(float val)
{
     buffer[head] = val;   //stores a value in current head position
        head++;               //head lai agi badauni to point next position
        if(head == max_size)
        {
            head = 0;   //head last position ma pugyo vane aba head lai 0 ma lagni
        }
        if(count != max_size)
        {
            count++;     //buffer ko size full vaye paxi count badhdaina
        }
}

bool RingBuffer::is_ready()
{
    if(count==max_size)
        {
            return true;
        }
        return false;
}

float RingBuffer::get(int index)
{
     return buffer[index];
}

void RingBuffer::get_batch(float* output_array)
{
    for(int i=0;i<max_size;i++)
        {
            int index = (head + i) % 50;
            output_array[i] = buffer[index];
        }
}