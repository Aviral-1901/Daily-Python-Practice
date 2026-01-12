**TINY ML WALK DETECTOR (ESP32 + MPU6050)**

Abstract:
This project implements a neural network from scratch in C++ to detect walking vs sitting.
No external libraries used. Built using raw linear algebra.

Features:
Circular buffer for real-time streaming.
High Pass Filter for gravity removal.
Latency < 100ms

Hardware:
ESP32 
MPU6050 Accelerometer

Memory Usage:
RAM : About 516 bytes -> Ringbuffer: 208bytes, NeuralNetwork class - 40bytes, main - about 270bytes
Flash: 2084bytes(weights + biases)

Conclusion:
ESP32(320,000 bytes): 0.1% RAM Usage
ArduinoUno(2048 bytes): 25% RAM Usage 
