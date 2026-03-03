#include <stdio.h>
#include <cstring>
#include "knn.h" 
#include "Arduino.h"

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
    float top_dist[3] = {INFINITY, INFINITY, INFINITY};
    int top_labels[3] = {-1, -1, -1};
    for(int i=0;i<count;i++)
    {
        float dist = get_distance(input_features, database[i].data);
        if (dist < top_dist[0]) 
        {
            //push 1st to 2nd, 2nd to 3rd
            top_dist[2] = top_dist[1]; top_labels[2] = top_labels[1];
            top_dist[1] = top_dist[0]; top_labels[1] = top_labels[0];
            //get 1st place
            top_dist[0] = dist; top_labels[0] = database[i].label;
            } 

            else if (dist < top_dist[1]) 
            {
            //push 2nd to 3rd
            top_dist[2] = top_dist[1]; top_labels[2] = top_labels[1];
            //get 2nd place
            top_dist[1] = dist; top_labels[1] = database[i].label;
            }

            else if (dist < top_dist[2]) 
            {
            //claim 3rd place
            top_dist[2] = dist; top_labels[2] = database[i].label;
            }
    }

    int votes_yes = 0;
    int votes_no = 0;

    for (int j = 0; j < 3; j++) 
    {
        if (top_labels[j] == 1) votes_yes++;
        if (top_labels[j] == 0) votes_no++;
    }

    if (votes_yes > votes_no) return 1;
    return 0;
}