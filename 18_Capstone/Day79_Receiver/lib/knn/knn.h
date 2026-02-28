#ifndef KNN_H
#define KNN_H

#include <stdio.h>
#include <cstring>

float get_distance(float* A, float* B);


struct  Exempler
{
    float data[488];
    int label;
};


class KNNClassifier
{
    Exempler database[10];
    int count;
    int k = 3;
    
    public:
    KNNClassifier();
    
    void learn(float* new_features, int label);
   

    int predict(float* input_features);
 
};

#endif