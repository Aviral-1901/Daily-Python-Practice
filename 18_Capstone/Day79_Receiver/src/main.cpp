#include <Arduino.h>
#include "knn.h"

KNNClassifier my_knn;

void process_packet()
{
  uint8_t command;
  Serial.readBytes(&command, 1); //READ COMMAND , 1 byte only
  uint8_t label;
  Serial.readBytes(&label, 1);   //read label
  float features[488]; //488 floats = 1952 bytes
  //serial.readBytes bata ek choti euta matra byte lina milxa
  //float 4 bytes ko hunxa 
  //tei vayera byte pointer liyera one byte gardai features array ma value fill garni
  uint8_t* byte_ptr = (uint8_t*) features; 
  int bytes_read = Serial.readBytes(byte_ptr, 1952); //Serial.readBytes le number of bytes pani return garxa
  //1952 vaneko total 1952 bytes read garna vaneko
  if(bytes_read != 1952) return;
  if(command==1) 
  {
    my_knn.learn(features, label);
    Serial.println("Learned");
    Serial.println(features[0], 4);
  }
  if(command==2) 
  {
    int prediction = my_knn.predict(features);
    Serial.printf("Predicted: %d\n",prediction);
  }
}

void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(5000); //dont wait for more than 2sec for reading Bytes
}


void loop()
{
  if(Serial.available() > 0) //check for data in the buffer
  {
    char c = Serial.read(); //read one character
    if(c == 'S') //check if the first character is 'S'
    {
      char header[4];
      Serial.readBytes(header, 4); //check if other characters are T,A,R,T
      if(header[0] == 'T' && header[1]=='A' && header[2]=='R' && header[3]=='T')
      {
        process_packet();
      }
    }
  }
}