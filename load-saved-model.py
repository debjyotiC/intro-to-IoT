import tensorflow as tf
import numpy as np

x_test = np.array([102], dtype='float32')

# load Keras model
load_model = tf.keras.models.load_model('saved_model/tf_model_2')
classes = load_model.predict(np.vstack([x_test]))
print(classes[0][0])

