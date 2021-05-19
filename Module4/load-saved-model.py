import tensorflow as tf
import numpy as np

x_test = np.array([100], dtype='float32')

# lead keras model
loaded_model = tf.keras.models.load_model('saved_model/tf_model_2')

classes = loaded_model.predict(np.vstack([x_test]))[0][0]

print(classes)
