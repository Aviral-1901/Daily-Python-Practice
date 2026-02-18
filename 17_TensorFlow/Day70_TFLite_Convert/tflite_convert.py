import tensorflow as tf
import keras
from keras import models

model = models.load_model(r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day70_TFLite_Convert\audio_model.h5")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

output_path = r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day70_TFLite_Convert\audio_model.tflite"
with open(output_path, 'wb') as f:
    f.write(tflite_model)


model.summary()