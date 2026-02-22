import os
os.environ['TF_USE_LEGACY_KERAS'] = '1'

import numpy as np
import tensorflow as tf
import tf_keras as keras
import tensorflow_model_optimization as tfmot


with tfmot.quantization.keras.quantize_scope():
    qat_model = keras.models.load_model(r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day74_QAT_Convert\qat_model.h5")

    converter = tf.lite.TFLiteConverter.from_keras_model(qat_model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.inference_input_type = tf.int8
    converter.inference_output_type = tf.int8

    tflite_model = converter.convert()
    output_path = r"C:\Users\Dell\Desktop\PYTHON Daily\17_TensorFlow\Day74_QAT_Convert\qat_audio.tflite"
    with open(output_path, 'wb') as f:
        f.write(tflite_model)