import tensorflow as tf
saved_model_dir = 'saved_model/tf_model_2'

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)

tflite_model = converter.convert()
open("saved_model/converted_model.tflite", "wb").write(tflite_model)
