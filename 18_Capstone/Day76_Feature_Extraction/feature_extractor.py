import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import numpy as np
import tensorflow as tf
import tf_keras as keras
import tensorflow_model_optimization as tfmot

X = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day76_Feature_Extraction\X_data.npy")
Y = np.load(r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day76_Feature_Extraction\Y_labels.npy")

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(
    filters= 8,
    kernel_size=(129, 3),
    activation='relu',
    input_shape = (129, 124, 1)
))

model.add(keras.layers.MaxPool2D(pool_size=(1,2)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, Y, epochs=20, batch_size=2)

#we create a new model from the above trained model with same input but outputs the flatten layer output
extractor = keras.Model(inputs=model.input, outputs=model.layers[2].output)
print("Extractor output shape :",extractor.output_shape)
converter = tf.lite.TFLiteConverter.from_keras_model(extractor)
tflite_model = converter.convert()

output_path = r"C:\Users\Dell\Desktop\PYTHON Daily\18_Capstone\Day76_Feature_Extraction\extraced.tflite"
with open(output_path, 'wb') as f:
    f.write(tflite_model)