#include <stdio.h>

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
    RingBuffer3D()
    {
        head = 0;
        count = 0;
    }
    
    void add(float x, float y, float z)
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

    void get_batch(Point3D* output)
    {
        for(int i=0; i<111; i++)
        {
            int index = (head + i) % 111;
            output[i] = buffer[index]; 
        }
    }

    bool is_ready()   //to check whether buffer is full or not
    {
        return count >= 111;
    }

};

int main()
{
    Point3D batch[111];
    RingBuffer3D rbuffer;
    for(int i=0; i<115; i++)
    {
        rbuffer.add(i, i, i);
        if(rbuffer.is_ready())
            rbuffer.get_batch(batch);   
    }

    printf("Oldest (Index 0): %f\n", batch[0].x);
    printf("Newest (Index 110): %f\n", batch[110].x);

}