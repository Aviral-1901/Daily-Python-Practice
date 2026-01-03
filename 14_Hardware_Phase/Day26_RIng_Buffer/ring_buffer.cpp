#include<iostream>
using namespace std;

class RingBuffer
{   
    public:
    float buffer[50];  //buffer arrays where the values will be stored
    int head;          //head le next value kaha store garne position store garxa
    int count;         //count stores how many valid values we have in the buffer
    const int max_size = 50;  //buffer ko maximum size
    
    public:
    RingBuffer()
    {
        head = 0;    //at first head points at position 0
        count = 0;   //at first buffer is empty so count is 0
        for(int i=0; i<50; i++)
        {
            buffer[i] = 0.0;   //buffer ko sab index ma 0 haleko garbage na aaos vanera
        }
    }

    void add(float val)
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

    bool is_ready()   //to check whether buffer is full or not
    {
        if(count==max_size)
        {
            return true;
        }
        return false;
    }

    float get(int index)   //return value at specific index of the buffer
    {
        return buffer[index];
    }
};

int main()
{
    RingBuffer rbuffer;

    for(int i=0; i<55; i++)
    {
        rbuffer.add(float(i));
        cout<<"Added: "<<i<< " Head is at: "<<rbuffer.head<< " Count: "<<rbuffer.count <<"\n";
    }
}