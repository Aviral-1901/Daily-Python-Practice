#include <stdio.h>
#include <cstring>
#include "knn.h" 

float get_distance(float* A, float* B)
{
    float total = 0.0;
    for(int i=0; i<488; i++)
    {
        float diff = A[i] - B[i];
        total += diff * diff;
    }
    return total;
}

KNNClassifier::KNNClassifier()
{
    count = 0;
}

void KNNClassifier::learn(float* new_features, int label)
{
    if(count < 10)
    {
        memcpy(database[count].data, new_features, 488*sizeof(float));
        database[count].label = label;
        count++;
    }
}

int KNNClassifier::predict(float* input_features)
{
    float min_dist = 99999.99;
    int best_label = -1;
    for(int i=0; i<count; i++)
    {
        float dist = get_distance(input_features, database[i].data);
        if(dist < min_dist) 
        {
            min_dist = dist;
            best_label = database[i].label;
        }
    }
    return best_label;
}