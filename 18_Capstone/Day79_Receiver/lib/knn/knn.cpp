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

void KNNClassifier::learn(float* new_features, int label) {
    if(count < 10) {
        //save to RAM
        memcpy(database[count].data, new_features, 488 * sizeof(float));
        database[count].label = label;
        count++;
        
        Serial.println("RAM Update Complete. Attempting Flash Save...");

        //save to Flash
        if (prefs.begin("AI_Memories", false)) { // Open Namespace
            
            //save Count
            size_t count_bytes = prefs.putInt("count", count);
            
            //save Exempler
            String key = "mem_" + String(count - 1);
            size_t blob_bytes = prefs.putBytes(key.c_str(), &database[count-1], sizeof(Exempler));
            
            prefs.end(); // Close
            
            //verify
            if (count_bytes > 0 && blob_bytes > 0) {
                Serial.printf("Flash Save SUCCESS! Key: %s, Size: %d\n", key.c_str(), blob_bytes);
            } else {
                Serial.println("Flash Save FAILED: Wrote 0 bytes.");
            }
            
        } else {
            Serial.println("Error: Could not open NVS Namespace for writing.");
        }
        
    } else {
        Serial.println("Error: Database Full!");
    }
}

int KNNClassifier::predict(float* input_features)
{
    float top_dist[3] = {INFINITY, INFINITY, INFINITY};
    int top_labels[3] = {-1, -1, -1};
    for(int i=0; i<count; i++)
    {
        float dist = get_distance(input_features, database[i].data);
        if (dist < top_dist[0]) 
        {
            // Push 1st to 2nd, 2nd to 3rd
            top_dist[2] = top_dist[1]; top_labels[2] = top_labels[1];
            top_dist[1] = top_dist[0]; top_labels[1] = top_labels[0];
            // Claim 1st place
            top_dist[0] = dist; top_labels[0] = database[i].label;
        } 

        else if (dist < top_dist[1]) 
        {
            // Push 2nd to 3rd
            top_dist[2] = top_dist[1]; top_labels[2] = top_labels[1];
            // Claim 2nd place
            top_dist[1] = dist; top_labels[1] = database[i].label;
        }
        else if (dist < top_dist[2]) 
        {
            // Claim 3rd place
            top_dist[2] = dist; top_labels[2] = database[i].label;
        }
    }

    int votes_yes = 0;
    int votes_no = 0;

    for (int j = 0; j < 3; j++) {
        if (top_labels[j] == 1) votes_yes++;
        if (top_labels[j] == 0) votes_no++;
    }

    if (votes_yes > votes_no) return 1;
    return 0;
}

void KNNClassifier::load_from_flash() {
    // Open in Read/Write mode to ensure it exists
    prefs.begin("AI_Memories", false); 
    
    count = prefs.getInt("count", 0); // Default to 0 if not found
    
    Serial.printf("\nNVS LOAD \n");
    Serial.printf("Memories Found: %d\n", count);
    
    for(int i = 0; i < count; i++) {
        String key = "mem_" + String(i);
        size_t bytes_read = prefs.getBytes(key.c_str(), &database[i], sizeof(Exempler));
        
        if (bytes_read == sizeof(Exempler)) {
            Serial.printf("Loaded memory %d (Label: %d)\n", i, database[i].label);
        } else {
            Serial.printf("FAILED to load memory %d\n", i);
        }
    }
    prefs.end();
    Serial.printf("----------------\n");
}

void KNNClassifier::clear_memory() {
    prefs.begin("AI_Memories", false); //open in Read/Write mode
    prefs.clear();                     //delete everything in this drawer
    prefs.end();                       //close drawer
    
    count = 0;                         //reset the RAM counter too!
    Serial.println("Memory completely erased.");
}