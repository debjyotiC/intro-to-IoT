import tensorflow as tf
import numpy as np

x_test = np.array([100], dtype='float32')

# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="saved_model/converted_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

test = np.vstack([x_test])
interpreter.set_tensor(input_details[0]['index'], test)

interpreter.invoke()
classes = interpreter.get_tensor(output_details[0]['index'])
print(classes)
