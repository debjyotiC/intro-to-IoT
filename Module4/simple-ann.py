import tensorflow as tf
import numpy as np

xs = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)  # i/p data
ys = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)  # labels

l0 = tf.keras.layers.Dense(units=1, input_shape=[1])  # def NN

model = tf.keras.Sequential([l0])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))

model.fit(xs, ys, epochs=600)

print("Weights are:{}".format(l0.get_weights()))

print(model.predict([100]))
