#ifndef RING_BUFFER_3D_H
#define RING_BUFFER_3D_H

struct Point3D
{
    float x; float y; float z;
};

class RingBuffer3D
{
    int head = 0;
    int count = 0;
    Point3D buffer[111] = {};

    public:
    RingBuffer3D();
    
    void add(float x, float y, float z);

    void get_batch(Point3D* output);

    bool is_ready();  //to check whether buffer is full or not
};

#endif
