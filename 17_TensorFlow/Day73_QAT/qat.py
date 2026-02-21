import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import numpy as np
import tensorflow as tf
import tf_keras as keras
import tensorflow_model_optimization as tfmot

X = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day72_QAT\X_data.npy")
Y = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day72_QAT\Y_labels.npy")

model = keras.models.Sequential() #sequential euta container ho jasma layers are stacked one after another
model.add(keras.layers.Conv2D (
    filters = 8,
    kernel_size = (129, 3), #to cover all the frequencies and 3 time stamps at a time
    activation = 'relu',
    input_shape = (129, 124, 1)
) )

model.add(keras.layers.MaxPool2D(pool_size=(1, 2))) #time axis lai half garxa 
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(1, activation='sigmoid'))

#training ko lagi rule set garxa compile le
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) 
#adam for adaptive learning rate and binary crossentropy to punish wrong guesses

model.fit(X, Y, epochs=20, batch_size=2)

quantize_model = tfmot.quantization.keras.quantize_model
q_aware_model = quantize_model(model)

q_aware_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
q_aware_model.fit(X, Y, epochs=10, batch_size=2)
q_aware_model.save(r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day72_QAT\qat_model.h5")
q_aware_model.summary()