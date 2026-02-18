import numpy as np
import keras
from keras import layers, models

X = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day69_TF_Intro\X_data.npy")
Y = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day69_TF_Intro\Y_labels.npy")

print(X.shape)

model = models.Sequential() #sequential euta container ho jasma layers are stacked one after another
model.add(layers.Conv2D (
    filters = 8,
    kernel_size = (129, 3), #to cover all the frequencies and 3 time stamps at a time
    activation = 'relu',
    input_shape = (129, 124, 1)
) )

model.add(layers.MaxPool2D(pool_size=(1, 2))) #time axis lai half garxa 
model.add(layers.Flatten())
model.add(layers.Dense(1, activation='sigmoid'))

#training ko lagi rule set garxa compile le
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) 
#adam for adaptive learning rate and binary crossentropy to punish wrong guesses

model.fit(X, Y, epochs=20, batch_size=2)
#start training , run 20 full passes of data -forward and backward, and updates weights every 2 samples

model.summary()
