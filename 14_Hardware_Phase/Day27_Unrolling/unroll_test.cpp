/*
 * ======================================================================================
 * ARCHITECTURAL DECISION: UNROLLING (COPY) VS TAIL POINTER (ZERO-COPY)
 * ======================================================================================
 *
 * PROBLEM:
 * The Ring Buffer stores data in circular order due to wrapping.
 * The Neural Network requires inputs in strict chronological order
 * (Oldest -> Newest) and reuses the same input window multiple times.
 *
 * STRATEGY A: ZERO-COPY (Direct Ring Buffer Access)
 * - Logic: Access buffer using circular indexing inside the NN inner loops.
 *          Example: buffer[(tail + i) % 50]
 * - Cost: 0 copy operations.
 * - Penalty: Circular index arithmetic is executed inside hot NN loops
 *            (50 inputs × 10 neurons = 500 indexed accesses).
 * - Impact: Adds extra address calculations and prevents the compiler from
 *           applying aggressive optimizations (loop unrolling, vectorization).
 *
 * STRATEGY B: UNROLLING (Current Implementation)
 * - Logic: Copy the ring buffer into a clean, linear array ONCE per inference.
 * - Cost: 50 copy operations.
 * - Benefit: Neural network loops perform simple, predictable linear memory access.
 * - Impact: Enables better compiler optimization and keeps NN math loops minimal.
 *
 * DECISION:
 * Pay a small one-time copy cost (Unrolling) to simplify and speed up
 * the neural network inference path, which reuses the input data many times.
 * ======================================================================================
 */

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

    void get_batch(float* output_array)
    {
        for(int i=0;i<max_size;i++)
        {
            int index = (head + i) % 50;
            output_array[i] = buffer[index];
        }
    }
};

int main()
{
    RingBuffer rbuffer;
    for(int i=0;i<50;i++)
    {
        rbuffer.add(float(i));
    }

    rbuffer.add(50.0);
    rbuffer.add(51.0);
    rbuffer.add(52.0);
    rbuffer.add(53.0);
    rbuffer.add(54.0);
    
    float clean_data[50];   //to store chronological data from oldest to newest 
    rbuffer.get_batch(clean_data);

    for(int i=0;i<rbuffer.max_size;i++)
    {
        cout<<clean_data[i]<<"..";
    }

}