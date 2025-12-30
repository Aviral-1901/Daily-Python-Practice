import numpy as np
import matplotlib.pyplot as plt
from dense_layer_class import DenseLayer

#X and Y are labelled data like 1 for walk and 0 for sit
X = np.load( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\X_train.npy")
Y = np.load( r"C:\Users\Dell\Desktop\PYTHON Daily\13_Phyphox_Real_World\Y_train.npy")

#shuffle the data again
indices = np.arange(X.shape[0])
np.random.shuffle(indices)

X_shuffled = X[indices]
Y_shuffled = Y[indices]

#training with 80% data and evaluating on 20% data
splits = np.ceil(len(X) * 0.8).astype(int)

#X-train and Y_train are for training and X_val and Y_val are for testing the neuron
X_train_data = X_shuffled[:splits]
Y_train_data = Y_shuffled[:splits]
X_val_data = X_shuffled[splits:]
Y_val_data = Y_shuffled[splits:]

Layer1 = DenseLayer(50, 10)
Layer2 = DenseLayer(10, 1)

#training the neuron with 80% data 
for i in range(2000):
    out1 = Layer1.forward(X_train_data)
    out2 = Layer2.forward(out1)

    error = Y_train_data - out2

    grad2 = Layer2.backward(error,0.001)
    grad1 = Layer1.backward(grad2, 0.001)

#testing the neuron with 20% data which is X_val_data
hidden_output = Layer1.forward(X_val_data)
prediction = Layer2.forward(hidden_output)

TP = 0 #true positive -> target = 1, prediction = 1, walk predicted as walk
TN = 0 #true negative -> target = 0, prediction = 0, sit predicted as sit
FP = 0 #false positive -> target = 0, prediction = 1, sit predicted as walk
FN = 0 #false negative -> target = 1, prediction = 0, walk predicted as sit

for i in range(len(Y_val_data)):
    truth = Y_val_data[i][0]
    if prediction[i] > 0.5:  #taking values above 0.5 as 1 for walking
        guess = 1
    else:
        guess = 0
    
    if(truth == 1 and guess == 1):
        TP += 1
    if(truth == 0 and guess == 0):
        TN += 1
    if(truth == 0 and guess == 1):
        FP += 1
    if(truth == 1 and guess == 0):
        FN += 1   

print(f"TP : {TP}, TN : {TN}, FP : {FP}, FN : {FN}")
total = TP + TN + FP + FN

accuracy = (TP + TN) / total #how correct the ai predicted
precision = TP / (TP + FP)   #how trustoworthy is the neural network -> how reliable walk predictions are
recall = TP / (TP + FN)      #how many walks were detected

print(f"Accuracy : {accuracy}, precision : {precision}, recall : {recall}")