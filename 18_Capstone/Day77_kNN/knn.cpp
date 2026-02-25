#include <stdio.h>
#include <cstring>

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
    KNNClassifier()
    {
        count=0;
    }
    void learn(float* new_features, int label)
    {
        if(count < 10)
        {
            memcpy(database[count].data, new_features, 488*sizeof(float));
            database[count].label = label;
            count++;
        }
    }

    int predict(float* input_features)
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
};

int main()
{
    float vectorA[488];
    for(int i=0; i<488; i++) vectorA[i] = 1.0; 

    float vectorB[488];
    for(int i=0; i<488; i++) vectorB[i] = 0.0;

    KNNClassifier knn;
    knn.learn(vectorA, 1);
    knn.learn(vectorB, 0);

    float vectorC[488];
    for(int i=0; i<488; i++) vectorC[i] = 0.9;

    printf("The prediction is %d ",knn.predict(vectorC));
}