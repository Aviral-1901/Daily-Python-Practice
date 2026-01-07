#ifndef RING_BUFFER_H
#define RING_BUFFER_H

class RingBuffer
{   
    public:
    float buffer[50];  //buffer arrays where the values will be stored
    int head;          //head le next value kaha store garne position store garxa
    int count;         //count stores how many valid values we have in the buffer
    const int max_size = 50;  //buffer ko maximum size
    
    public:
    RingBuffer();

    void add(float val);
   

    bool is_ready();   //to check whether buffer is full or not
    
    float get(int index);   
    
    void get_batch(float* output_array);
};

#endif